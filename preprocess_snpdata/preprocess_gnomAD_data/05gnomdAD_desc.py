import os
import sys
import numpy as np


def is_nan_symbol(el):
    return el == "" or el == "-" or el == "."


ignore_attrs = ['True Label', 'CHROM', 'Nuc-Pos', 'REF-Nuc', 'ALT-Nuc', 'Ensembl-Gene-ID', 'Ensembl-Protein-ID',
                'Ensembl-Transcript-ID', 'Uniprot-Accession','Consequence','IMPACT','ClinVar_preferred_disease_name_in_CLNDISDB']
filename =sys.argv[1:][0]
if filename == "./clinvar/clinvar_20220620/02clinvar_20220620_selected_standard.csv":
    out_filename = "./clinvar/clinvar_20220620/03clinvar_20220620_selected_desc.csv"


test_mode = sys.argv[1:][1]
if test_mode == "missense":
    if filename == "./clinvar/clinvar_20230326/02clinvar_20230326_test_standard.csv":
        out_filename = "./clinvar/clinvar_20230326/03clinvar_20230326_test_desc.csv"
elif test_mode == "other_than_missense":
    if filename == "./gnomAD/02ExAC_for_other_than_missense_standard.csv":
        out_filename = "./gnomAD/03ExAC_for_other_than_missense_desc.csv"
    if filename == "./clinvar/clinvar_20220620/02clinvar_2022other_than_missense_test_standard.csv":
        out_filename = "./clinvar/clinvar_20220620/03clinvar_2022other_than_missense_test_desc.csv"

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
        m = np.nanmean(vec)
        s = np.nanstd(vec)
        statistics[k] = [m, s]
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
                bin_width = range_sigma / half_bin_num
                z = (x - m) / s
                y = z / bin_width
                if y > 0:
                    bin_n = np.ceil(y)
                    if bin_n > half_bin_num: bin_n = half_bin_num
                elif y < 0:
                    bin_n = np.floor(y)
                    if -bin_n > half_bin_num: bin_n = -half_bin_num

                # only bin number
                # desc_arr.append(str(bin_n))
                # constructing bin name
                if text_mode:
                    rec = k + ":" + str(int(bin_n)) + ":%.2f" % (m + bin_n * s)
                else:
                    rec = str(int(bin_n))
                desc_arr.append(rec)
            else:
                if text_mode:
                    rec = k + ":missing"
                else:
                    rec = str(0)
                desc_arr.append(rec)
        else:
            desc_arr.append(el)
    l = ",".join(desc_arr)
    out_fp.write(l)
    out_fp.write("\n")
