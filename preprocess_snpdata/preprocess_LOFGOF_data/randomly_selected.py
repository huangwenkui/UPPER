import random
import sys
csv_file = sys.argv[1:][0]
if csv_file == "./LOF_GOF/Classify_GOF_LOF_getdata.csv":
    out_file = "./LOF_GOF/Classify_GOF_LOF_test.csv"
    train_file = "./LOF_GOF/Classify_GOF_LOF_train.csv"

csv_fp =open(csv_file,'r')
out_fp =open(out_file,'w')
train_fp = open(train_file,'w')
lineset= set()
lines=csv_fp.readlines()
for i in range(0,10000):
    randline = random.randint(0,len(lines))
    lineset.add(randline)
    if len(lineset)>501:
        break
fp = open(csv_file,'r')
head = next(fp)
out_fp.write(head)
train_fp.write(head)
head_arr = head.strip().split(",")
header_mapping = {el: i for i, el in enumerate(head_arr)}
for i,line in enumerate(fp):
    if i in lineset:
        out_fp.write(line)
    else:
        train_fp.write(line)

