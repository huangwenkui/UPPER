import os
import sys
import numpy as np


def is_nan_symbol(el):
    return el == "" or el == "-" or el == "."


ignore_attrs = ['True Label', 'CHROM', 'Nuc-Pos', 'REF-Nuc', 'ALT-Nuc', 'Ensembl-Gene-ID', 'Ensembl-Protein-ID',
                'Ensembl-Transcript-ID', 'Uniprot-Accession','Consequence','IMPACT',"Amino_acids", "cDNA_position",'BIOTYPE',
                'GERP_RS_rankscore','GenoCanyon_rankscore','DANN_rankscore','FATHMM_converted_rankscore','MutationTaster_converted_rankscore',
                'fathmm_MKL_coding_rankscore','phastCons100way_vertebrate_rankscore',
                "CDS_position","Protein_position","Codons","DOMAINS","kGp3_AF","ExAC_AF","gnomAD_exomes_AF",'ClinVar_preferred_disease_name_in_CLNDISDB']
filename =sys.argv[1:][0]
test_mode = sys.argv[1:][1]
if test_mode == "missense":
    if filename == "./PPARG/PPARG_test.csv":
        out_filename = "./PPARG/00PPARG_desc.csv"


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
# for k, vec in all_data.items():
#     try:
#         # m = np.nanmean(vec)
#         # s = np.nanstd(vec)
#         max = np.nanmax(vec)
#         min = np.nanmin(vec)
#         statistics[k] = [max, min]
#         # print(k, max, min)
#     except:
#         print(k)

fp = open(filename)
head = next(fp)
head_arr = head.strip().split(",")
header_mapping = {el: i for i, el in enumerate(head_arr)}
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
                y = x*10
                if y >9.9:
                    bin_n = 10
                else:
                    bin_n = np.floor(y)
                rec = str(int(bin_n))
                desc_arr.append(rec)
            else:
                if text_mode:
                    rec = k + ":missing"
                else:
                    rec = "5"
                    # rec = str(0)
                desc_arr.append(rec)
        else:
            desc_arr.append(el)
    l = ",".join(desc_arr)
    out_fp.write(l)
    out_fp.write("\n")


