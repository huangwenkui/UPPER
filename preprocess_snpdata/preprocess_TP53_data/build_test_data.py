import sys

def make_key_id(CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc):
    l = [CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc]
    key_id = "_".join(l)
    return key_id


label_mapping = {"Likely_benign": "-1", "Benign": "-1" , "Likely_pathogenic": "1", "Pathogenic": "1","-1":"-1","1":"1"}
# True Label
train_id_data = set()

clinvar_2022_idfilename = './03data_graph/clinvar_2022_all/var.label.tsv'
clfp = open(clinvar_2022_idfilename)
for line in clfp:
    arr = line.strip().split("\t")
    train_id_data.add(arr[0])


out_filename = "./TP53/TP53_test_for_vep.tsv"
out_fp = open(out_filename, "w")
filename1 = sys.argv[1:][0]
fp1 = open(filename1)
for line in fp1:
    arr = line.strip().split("\t")
    CHROM = arr[0]
    Nuc_Pos =arr[1]
    temp= arr[3].split("/")
    REF_Nuc = temp[0]
    ALT_Nuc =temp[1]
    key_id = make_key_id(CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc)
    num_temp1 = len(train_id_data)
    train_id_data.add(key_id)
    num_temp2 = len(train_id_data)
    if num_temp1 == num_temp2:
        continue
    out_fp.write(line)
filename2 = sys.argv[1:][1]
fp1 = open(filename2)
for line in fp1:
    arr = line.strip().split("\t")
    CHROM = arr[0]
    Nuc_Pos =arr[1]
    temp= arr[3].split("/")
    REF_Nuc = temp[0]
    ALT_Nuc =temp[1]
    key_id = make_key_id(CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc)
    num_temp1 = len(train_id_data)
    train_id_data.add(key_id)
    num_temp2 = len(train_id_data)
    if num_temp1 == num_temp2:
        continue
    out_fp.write(line)
