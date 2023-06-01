import os
import sys


train_filename1 = sys.argv[1:][0]
train_filename2 = sys.argv[1:][1]
train_feature_path1 = os.path.join(train_filename1, str("feature.graph.tsv"))
train_feature_path2 = os.path.join(train_filename2, str("feature.graph.tsv"))
train_id_path1 = os.path.join(train_filename1, str("id.graph.tsv"))
train_id_path2 = os.path.join(train_filename2, str("id.graph.tsv"))
train_label_path1 = os.path.join(train_filename1, str("var.label.tsv"))
train_label_path2 = os.path.join(train_filename2, str("var.label.tsv"))

if train_filename1 =="./03data_graph/clinvar_20220620":
    name = "clinvar_2022"
elif train_filename1 =="./03data_graph/gnomAD_for_other_than_missense":
    name = "gnomAD_with_clinvar_2023"
elif train_filename1 =="./03data_graph/clinvar_2022":
    name = "clinvar_2022_all"

output_path = "03data_graph/" + name + "/"
os.makedirs(output_path, exist_ok=True)

feature_KG = []
for term in [train_feature_path1, train_feature_path2]:
    with open(term, "r") as rf:
        for line in rf.readlines():
            line = line.strip().split("\t")
            feature_KG.append(line)

id_KG = []
for term in [train_id_path1,train_id_path2]:
    with open(term, "r") as rf:
        for line in rf.readlines():
            line = line.strip().split("\t")
            id_KG.append(line)

label_KG = []
for term in [train_label_path1, train_label_path2]:
    with open(term, "r") as rf:
        for line in rf.readlines():
            line = line.strip().split("\t")
            label_KG.append(line)


out_fp = open(output_path + "feature.graph.tsv", "w")
for pair in feature_KG:
    s = "\t".join(pair)
    out_fp.write(s)
    out_fp.write("\n")


out_fp = open(output_path + "var.label.tsv", "w")
for pair in label_KG:
    s = "\t".join(pair)
    out_fp.write(s)
    out_fp.write("\n")

out_fp = open(output_path + "id.graph.tsv", "w")
for i in id_KG:
    s = "\t".join(i)
    out_fp.write(s)
    out_fp.write("\n")
