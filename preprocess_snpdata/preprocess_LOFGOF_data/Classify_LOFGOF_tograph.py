import os
import sys
import numpy as np

ignore_attrs = ['LOFGOF', 'CHROM', 'Nuc-Pos', 'REF-Nuc', 'ALT-Nuc', 'Ensembl-Gene-ID', 'Ensembl-Protein-ID',
                'Ensembl-Transcript-ID', 'Uniprot-Accession','Consequence','IMPACT','ClinVar_preferred_disease_name_in_CLNDISDB',
                'cDNA_position','CDS_position','Protein_position','VARIANT_CLASS','DOMAINS_VEP']
label_name = "LOFGOF"
label_mapping = {'LOF':'1','GOF':'-1'}


def is_nan_symbol(el):
    return el == "" or el == "-" or el == "."


def make_key_id(head_mapping, arr):
    l = [arr[i].strip("chr") for i in
         [head_mapping["CHROM"], head_mapping["Nuc-Pos"], head_mapping["REF-Nuc"], head_mapping["ALT-Nuc"]]]
    key_id = "_".join(l)
    return key_id

filename =sys.argv[1:][0]
if filename == "./LOF_GOF/Classify_GOF_LOF_train.csv":
    name = "LOFGOF_train"
elif filename == "./LOF_GOF/Classify_GOF_LOF_test.csv":
    name = "LOFGOF_test"
else:
    print("error")

id_data = []
score_data = []
label_data = []
fp = open(filename)
head = next(fp)
head_arr = head.strip().split(",")

header_mapping = {el: i for i, el in enumerate(head_arr)}

for line in fp:
    arr = line.strip().split(",")
    # for index
    key_id = make_key_id(header_mapping, arr)
    # for data: "Ensembl-Gene-ID"
    id_name = 'Ensembl-Gene-ID'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'Ensembl-Gene-ID', "ENSEMBL:" + el])
                tep_set.add(el)

    # for data: "Ensembl-Protein-ID"
    id_name = 'Ensembl-Protein-ID'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'Ensembl-Protein-ID', "ENSEMBL:" + el])
                tep_set.add(el)

    # for data: "Ensembl-Transcript-ID"
    id_name = 'Ensembl-Transcript-ID'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'Ensembl-Transcript-ID', "ENSEMBL:" + el])
                tep_set.add(el)

    # for data: "Uniprot_id"
    id_name = 'Uniprot-Accession'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'Uniprot-Accession', "uniprotkb:" + el])
                tep_set.add(el)
    # for ClinVar_preferred_disease_name_in_CLNDISDB
    id_name = 'ClinVar_preferred_disease_name_in_CLNDISDB'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?") & (el != "not_provided")&(el != "See_cases")&(el != "not_specified")&(el != ""):
            if el not in tep_set:
                id_data.append([key_id, 'ClinVar_preferred_disease_name_in_CLNDISDB', el])
                tep_set.add(el)
    # for Consequence
    id_name = 'Consequence'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'Consequence', el])
                tep_set.add(el)
    # for IMPACT
    id_name = 'IMPACT'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("&"):
        if (el != ".") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'IMPACT', el])
                tep_set.add(el)
    # for DOMAINS_VEP
    id_name = 'DOMAINS_VEP'
    id_index = header_mapping[id_name]
    id_el = arr[id_index]
    tep_set = set()
    for el in id_el.split("|"):
        if (el != "-") & (el != "?"):
            if el not in tep_set:
                id_data.append([key_id, 'DOMAINS_VEP', el])
                tep_set.add(el)

    # for position
    id_names = ['cDNA_position','CDS_position','Protein_position']
    for id_name in id_names:
        id_index = header_mapping[id_name]
        id_el = arr[id_index]
        if (id_el != ".") & (id_el != "-"):
            tem_arr = id_el.split("/")
            try:
                tem1=float(tem_arr[0])
                tem2=float(tem_arr[1])
                p = str(int(round(tem1/tem2,2)*10)*10)+"%"
                score_data.append([key_id, id_name, p])
            except:
                continue

    # for other data
    for i, el in enumerate(arr):
        k = head_arr[i]
        if not k in ignore_attrs and not is_nan_symbol(el):
            score_data.append([key_id, k, el])
    # for REF-AA
    # for ALT-AA
    # for label
    label_index = header_mapping[label_name]
    label_el = arr[label_index]
    label_arr = set(label_el.split("|"))
    if len(label_arr) == 1:
        el = label_mapping[list(label_arr)[0]]
        label_data.append([key_id, el])

output_path = "03data_graph/" + name + "/"
os.makedirs(output_path, exist_ok=True)
# print(len(score_data))
out_fp = open(output_path + "feature.graph.tsv", "w")
for pair in score_data:
    s = "\t".join(pair)
    out_fp.write(s)
    out_fp.write("\n")

# print(len(id_data))
out_fp = open(output_path + "id.graph.tsv", "w")
for pair in id_data:
    s = "\t".join(pair)
    out_fp.write(s)
    out_fp.write("\n")

# print(len(label_data))
out_fp = open(output_path + "var.label.tsv", "w")
for pair in label_data:
    s = "\t".join(pair)
    out_fp.write(s)
    out_fp.write("\n")
