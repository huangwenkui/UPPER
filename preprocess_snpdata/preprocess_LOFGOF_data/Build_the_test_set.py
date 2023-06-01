import sys

def make_key_id(head_mapping, arr):
    l = [arr[i].strip("chr") for i in
         [head_mapping["CHROM"], head_mapping["Nuc-Pos"], head_mapping["REF-Nuc"], head_mapping["ALT-Nuc"]]]
    key_id = "_".join(l)
    return key_id


label_mapping = {"Likely_benign": "-1", "Benign": "-1" , "Likely_pathogenic": "1", "Pathogenic": "1","-1":"-1","1":"1","0":"-1"}
# True Label
train_id_data = set()


clinvar_2022_idfilename = './03data_graph/clinvar_2022_all/var.label.tsv'
clfp = open(clinvar_2022_idfilename)
for line in clfp:
    arr = line.strip().split("\t")
    train_id_data.add(arr[0])

filename = sys.argv[1:][0]
# print(filename)
# print(test_mode)

if filename == "./clinvar/clinvar_20230326/00clinvar_20230326_selected.csv":
    out_filename = "./clinvar/clinvar_20230326/00clinvar_20230326_test.csv"
elif filename == "./LOF_GOF/goflof_HGMD2019_with_gnomAD.csv":
    out_filename = "./LOF_GOF/goflof_HGMD2019_with_gnomAD_test.csv"


out_fp = open(out_filename, "w")
fp = open(filename)
head = next(fp)
out_fp.write(head)
head_arr = head.strip().split(",")
header_mapping = {el: i for i, el in enumerate(head_arr)}
P_label = 0
B_label = 0
for line in fp:
    arr = line.strip().split(",")
    key_id = make_key_id(header_mapping, arr)
    num_temp1 = len(train_id_data)
    train_id_data.add(key_id)
    num_temp2 = len(train_id_data)
    if num_temp1 == num_temp2:
        continue
    label = label_mapping[arr[header_mapping['True Label']]]
    if label=="-1":
        B_label += 1
    elif label == "1":
        P_label +=1
    out_fp.write(line)
print(B_label)
print(P_label)