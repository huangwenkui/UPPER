'''
code for entity classification task
'''
from __future__ import division
from __future__ import print_function
import time
import tensorflow as tf
from utils import *
from metrics import *
from models import AutoRGCN_Align
import random
import logging
import os

# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ['CUDA_VISIBLE_DEVICES'] = "0,1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
# Settings
flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('dataset', 'exovar_filtered_tool_scores', 'Dataset: exovar_filtered_tool_scores, humvar_filtered_tool_scores.')
flags.DEFINE_string('mode', 'None', 'KE method for GCN: TransE, TransH, TransD, DistMult, RotatE, QuatE')
flags.DEFINE_string('optim', 'Adam', 'Optimizer: GD, Adam')
flags.DEFINE_float('learning_rate', 0.01, 'Initial learning rate.')
flags.DEFINE_integer('epochs', 500, 'Number of epochs to train.')
flags.DEFINE_float('dropout', 0., 'Dropout rate (1 - keep probability).')
flags.DEFINE_float('gamma', 3.0, 'Hyper-parameter for margin based loss.')
flags.DEFINE_integer('num_negs', 5, 'Number of negative samples for each positive seed.')
flags.DEFINE_float('alpha', 0.5, 'Weight of entity conv update.')
flags.DEFINE_float('beta', 0.5, 'Weight of relation conv update.')
flags.DEFINE_integer('layer', 0, 'number of hidden layers')
flags.DEFINE_integer('dim', 32, 'hidden Dimension')
flags.DEFINE_integer('randomseed', 12345, 'seed for randomness')
flags.DEFINE_boolean('rel_update', False, 'If true, use graph conv for rel update.')
flags.DEFINE_boolean('valid', False, 'If true, split validation data.')
flags.DEFINE_boolean('save', False, 'If true, save the print')
flags.DEFINE_string('metric', "cityblock", 'metric for testing')
flags.DEFINE_string('loss_mode', "L1", 'mode for loss calculation')
flags.DEFINE_string('embed', "random", 'init embedding for entities')

np.random.seed(FLAGS.randomseed)
random.seed(FLAGS.randomseed)
tf.compat.v1.set_random_seed(FLAGS.randomseed)

if FLAGS.save:
    nsave = "log/{}/{}".format(FLAGS.dataset, FLAGS.mode)
else:
    print("not saving file")
    nsave = "log/trash"
create_exp_dir(nsave)
log_format = '%(asctime)s %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format=log_format, datefmt='%m/%d %I:%M:%S %p', filemode="w")
save_fname = 'alpha{}-beta{}-layer{}-sdim{}-lr{}-seed{}'.format(
               FLAGS.alpha, FLAGS.beta, FLAGS.layer, FLAGS.dim,
               FLAGS.learning_rate, FLAGS.randomseed)

save_fname = "auto-" + save_fname
if not FLAGS.valid:
    save_fname = "test-" + save_fname
fh = logging.FileHandler(os.path.join(nsave, save_fname + ".txt"), "w")
fh.setFormatter(logging.Formatter(log_format))
logging.getLogger().addHandler(fh)
logging.getLogger().setLevel(logging.INFO)

# Load data
adj, num_ent, train, test, valid, y = load_data_class(FLAGS)
train = [train, y]
rel_num = np.max(adj[2][:, 1]) + 1
logging.info("Relation num: {}".format(rel_num))

# process graph to fit into later computation
support = [preprocess_adj(adj)]
num_supports = 1
model_func = AutoRGCN_Align
num_negs = FLAGS.num_negs
class_num = y.shape[1]
logging.info("Entity num: {}".format(num_ent))
logging.info("Class num: {}".format(class_num))

task = "class"
get_eval = get_class

# Define placeholders
placeholders = {
    'features': tf.compat.v1.placeholder(tf.float32),
    'dropout': tf.compat.v1.placeholder_with_default(0., shape=()),
    'num_features_nonzero': tf.compat.v1.placeholder_with_default(0, shape=())
}
placeholders['support'] = [[tf.compat.v1.placeholder(tf.float32, shape=[None, 1]),
                    tf.compat.v1.placeholder(tf.float32, shape=[None, 1]), \
                    tf.compat.v1.placeholder(tf.int32)] for _ in range(num_supports)]

# Create model
input_dim = [num_ent, rel_num]
hidden_dim = [FLAGS.dim, FLAGS.dim]
output_dim = [class_num, FLAGS.dim]
if FLAGS.mode == "TransH":
    hidden_dim[1] *= 2
elif FLAGS.mode == "TransD":
    hidden_dim[0] *= 2
    hidden_dim[1] *= 2
model = model_func(placeholders, input_dim, hidden_dim, output_dim, dataset=FLAGS.dataset,
                    train_labels=train, mode=FLAGS.mode, embed=FLAGS.embed, alpha=FLAGS.alpha,
                    beta=FLAGS.beta, layer_num=FLAGS.layer, sparse_inputs=False, featureless=True,
                    logging=True, rel_update=FLAGS.rel_update, task=task)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
epoch_best = 0
auc_best = 0.
# Train model

file_path = "results_data/{}/{}".format(FLAGS.dataset, FLAGS.mode)
create_exp_dir(file_path)
map_filename = os.path.join(file_path, save_fname + str(".txt"))

for epoch in range(FLAGS.epochs):
    # Construct feed dictionary
    feed_dict = construct_feed_dict(1.0, support, placeholders)
    feed_dict.update({placeholders['dropout']: FLAGS.dropout})
    # Training step
    outputs = sess.run([model.opt_op, model.loss], feed_dict=feed_dict)
    if valid is not None:
        # model.evaluate()
        output_embeddings = sess.run(model.outputs, feed_dict=feed_dict)
        train_evaluation = get_eval(output_embeddings[0], train[0], y, logging)
        valid_evaluation = get_eval(output_embeddings[0], valid, y, logging)
        if valid_evaluation['auc'] > auc_best:
            test_evaluation = get_eval(output_embeddings[0], test, y, logging)

            out_fp = open(map_filename, 'w')
            y_pre = output_embeddings[0][test]
            y_pre_sig = 1 / (1 + np.exp(-y_pre))
            y_pre_sig_list = [str(el[0]) for el in y_pre_sig.tolist()]
            l = "\n".join(y_pre_sig_list)
            out_fp.write(l)

            epoch_best = epoch
            auc_best = valid_evaluation['auc']
        if epoch - epoch_best > 10:
            logging.info("Early Stopping!")
            break
        # Print results
        logging.info("Epoch: {} train_loss= {:.5f}".format(epoch + 1, outputs[1]))
        logging.info("Train AUC: %.3f" % (train_evaluation['auc'] * 100))
        logging.info("Valid AUC: %.3f" % (valid_evaluation['auc'] * 100))

    if valid is None:
        # model.evaluate()
        output_embeddings = sess.run(model.outputs, feed_dict=feed_dict)
        train_evaluation = get_eval(output_embeddings[0], train[0], y, logging)
        test_evaluation = get_eval(output_embeddings[0], test, y, logging)
        if test_evaluation['auc'] > auc_best:

            out_fp = open(map_filename, 'w')
            y_pre = output_embeddings[0][test]
            y_pre_sig = 1 / (1 + np.exp(-y_pre))
            y_pre_sig_list = [str(el[0]) for el in y_pre_sig.tolist()]
            l = "\n".join(y_pre_sig_list)
            out_fp.write(l)

            epoch_best = epoch
            auc_best = test_evaluation['auc']
        if epoch - epoch_best > 10:
            logging.info("Early Stopping!")
            break
        # Print results
        logging.info("Epoch: {} train_loss= {:.5f}".format(epoch + 1, outputs[1]))
        logging.info("Train AUC: %.3f" % (train_evaluation['auc'] * 100))
        logging.info("Test AUC: %.3f" % (test_evaluation['auc'] * 100))


logging.info("Optimization Finished!Test AUC: {}  Test Acc: {} Test F1: {} Test average_precision: {}".
             format(round(test_evaluation['auc'] * 100, 2), round(test_evaluation['acc'] * 100, 2),
             round(test_evaluation['F1'] * 100, 2), round(test_evaluation['average_precision'] * 100, 2)))
