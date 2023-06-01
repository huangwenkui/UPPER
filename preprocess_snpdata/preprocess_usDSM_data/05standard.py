import os
import sys
import numpy as np
import math


def is_nan_symbol(el):
    if el == "" or el == "-" or el == ".":
        return True
    if math.isnan(float(el)):
        return True


ignore_attrs = ['True Label', 'CHROM', 'Nuc-Pos', 'REF-Nuc', 'ALT-Nuc', 'Ensembl-Gene-ID', 'Ensembl-Protein-ID',
                'Ensembl-Transcript-ID', 'Uniprot-Accession','Consequence','IMPACT',"Amino_acids", "cDNA_position","kGp3_AF","ExAC_AF","gnomAD_exomes_AF",
                "CDS_position","Protein_position","Codons","DOMAINS",'ClinVar_preferred_disease_name_in_CLNDISDB','BIOTYPE']
filename =sys.argv[1:][0]
test_mode = sys.argv[1:][1]
if test_mode == "synonymous":
    if filename == "./usDSM/usDSM_vepout.csv":
        out_filename = "./usDSM/01usDSM_standard.csv"
    elif filename == "./clinvar/clinvar_20220620/00clinvar_2022_synonymous.csv":
        out_filename = "./usDSM/01clinvar_2022_synonymous_standard.csv"


half_bin_num = 10
range_sigma = 3
text_mode = False
all_data = {}
fp = open(filename)
head = next(fp)
head_arr = head.strip().split(",")
header_mapping = {el: i for i, el in enumerate(head_arr)}
data = [[] for _ in head_arr]
for line in fp:
    arr = line.strip().split(",")
    for i, el in enumerate(arr):
        data[i].append(el)
for i, d in enumerate(data):
    if not head_arr[i] in ignore_attrs:
        vec = [np.nan if is_nan_symbol(el) else float(el) for el in d]
        if head_arr[i] not in all_data:
            all_data[head_arr[i]] = []
        all_data[head_arr[i]].extend(vec)
statistics = {}
for k, vec in all_data.items():
    try:
        max = np.nanmax(vec)
        min = np.nanmin(vec)
        statistics[k] = [max, min]
        # print(k, m, s)
    except:
        print(k)
fp = open(filename)
head = next(fp)
head_arr = head.strip().split(",")
header_mapping = {el: i for i, el in enumerate(head_arr)}
basename = os.path.basename(filename)
out_fp = open(out_filename, "w")
out_fp.write(head)
for line in fp:
    arr = line.strip().split(",")
    desc_arr = []
    for i, el in enumerate(arr):
        k = head_arr[i]
        if not k in ignore_attrs:
            if not is_nan_symbol(el):
                x = float(el)
                m = statistics[k][0]
                s = statistics[k][1]
                z = (x - s)/(m - s)
                y = z * 10
                if y > 9.5:
                    bin_n = 10
                else:
                    bin_n = np.floor(y)
                rec = str(int(bin_n))
                desc_arr.append(rec)
            else:
                rec = "5"
                # rec = str(0)
                desc_arr.append(rec)
        else:
            desc_arr.append(el)
    l = ",".join(desc_arr)
    out_fp.write(l)
    out_fp.write("\n")
