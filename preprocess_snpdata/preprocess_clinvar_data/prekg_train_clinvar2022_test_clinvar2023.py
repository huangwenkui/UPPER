import os
import sys
import numpy as np
import pickle as pkl
import random


def reorder(raw_list):
    order_dict = {}
    order = 0
    for item in raw_list:
        if item not in order_dict:
            order_dict[item] = order
            order += 1
    return order_dict


data = {}
KG = []
train_filename1 = sys.argv[1:][0]
test_filename = sys.argv[1:][1]
train_feature_path1 = os.path.join(train_filename1, str("feature.graph.tsv"))
test_feature_path = os.path.join(test_filename, str("feature.graph.tsv"))
train_id_path1 = os.path.join(train_filename1, str("id.graph.tsv"))
test_id_path = os.path.join(test_filename, str("id.graph.tsv"))
train_label_path1 = os.path.join(train_filename1, str("var.label.tsv"))
test_label_path = os.path.join(test_filename, str("var.label.tsv"))
reactome_path = "./03data_graph/reactome_db.graph.tsv"

with open(reactome_path, "r") as rf:
    for line in rf.readlines():
        line = line.strip().split("\t")
        if line[0] == line[2]:
            print("[skip self-loop]",line[0])
            continue
        KG.append(line)
for term in [train_id_path1, train_feature_path1, test_id_path, test_feature_path]:
    with open(term, "r") as rf:
        for line in rf.readlines():
            line = line.strip().split("\t")
            KG.append(line)

head_idx, rel_idx, tail_idx = [], [], []
KG_num = 0
for i in KG:
    head_idx.append(i[0])
    rel_idx.append(i[1])
    tail_idx.append(i[2])
    KG_num +=1
head_idx, rel_idx, tail_idx = set(head_idx), set(rel_idx), set(tail_idx)
print("num of head id: {}, rel id: {}, tail id: {}, KG id: {}".format(len(head_idx), len(rel_idx), len(tail_idx), KG_num))
ent = [i[0] for i in KG] + [i[2] for i in KG]
rel = [i[1] for i in KG]
ent_order = reorder(ent)
rel_order = reorder(rel)
new_KG = [[ent_order[i[0]], rel_order[i[1]], ent_order[i[2]]] for i in KG]

label_map = {'-1': 0, '1': 1}
label_num = 1
label_onehot = np.zeros([len(ent_order), label_num])
train_idx = []
test_idx = []
for term in [train_label_path1]:
    with open(term, "r") as rf:
        for line in rf.readlines():
            line = line.strip().split("\t")
            i = ent_order[line[0]]
            # j = label_map[line[1]]
            # label_onehot[i][j] = 1
            label_onehot[i]=label_map[line[1]]
            train_idx.append(i)

with open(test_label_path, "r") as rf:
    for line in rf.readlines():
        line = line.strip().split("\t")
        i = ent_order[line[0]]
        # j = label_map[line[1]]
        # label_onehot[i][j] = 1
        label_onehot[i] = label_map[line[1]]
        test_idx.append(i)
y = label_onehot
data = {'A': new_KG,
        'y': y,
        'train_idx': train_idx,
        'test_idx': test_idx,
        "e": len(ent_order)
        }

out_filename = os.path.join(str("./kgdata/class/"), str("train_") + os.path.basename(train_filename1)+ str("_test_") + os.path.basename(test_filename) + str("pro.pickle"))
with open(out_filename, 'wb') as handle:
    pkl.dump(data, handle, protocol=pkl.HIGHEST_PROTOCOL)

