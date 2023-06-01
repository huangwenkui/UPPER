import os
import sys


train_filename1 = sys.argv[1:][0]
train_filename2 = sys.argv[1:][1]


if train_filename1 =="./LOF_GOF/goflof_HGMD2019_vepout.csv":
    out_filename = "./LOF_GOF/goflof_HGMD2019_with_gnomAD.csv"

out_fp = open(out_filename, "w")


fp = open(train_filename2, "r")
head = next(fp)
head__arr = head.strip().split(",")
head__mapping = {el: i for i, el in enumerate(head__arr)}
new_head =[]
for i, el in enumerate(head__arr):
    if i == head__mapping["phyloP100way_vertebrate"]:
        continue
    new_head.append(el)
l = ",".join(new_head)
out_fp.write(l)
out_fp.write("\n")
for line in fp:
    line__arr = line.strip().split(",")
    new_line = []
    for i, el in enumerate(line__arr):
        if i == head__mapping["phyloP100way_vertebrate"]:
            continue
        new_line.append(el)
    l = ",".join(new_line)
    out_fp.write(l)
    out_fp.write("\n")


fp = open(train_filename1, "r")
head = next(fp)
head__arr = head.strip().split(",")
head__mapping = {el: i for i, el in enumerate(head__arr)}
for line in fp:
    line__arr = line.strip().split(",")
    new_line = []
    for i, el in enumerate(line__arr):
        if i == head__mapping["id"] or i == head__mapping["LOFGOF"]:
            continue
        new_line.append(el)
    l = ",".join(new_line)
    out_fp.write(l)
    out_fp.write("\n")
