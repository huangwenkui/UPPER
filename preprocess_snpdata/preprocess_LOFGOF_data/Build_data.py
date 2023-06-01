import os
import sys

if len(sys.argv[1:])==2:
    test_filename1 = sys.argv[1:][0]
    test_filename2 = sys.argv[1:][1]
    if test_filename1 == "./LOF_GOF/goflof_HGMD2019_vepout.csv":
        out_filename = "./LOF_GOF/goflof_HGMD2019_with_gnomAD.csv"
    elif test_filename1 == "./clinvar/clinvar_20230326/00clinvar_2023other_than_missense_test.csv":
        out_filename = "./clinvar/clinvar_20230326/00clinvar_2023other_than_missense_gnomAD_test.csv"
    out_fp = open(out_filename, "w")
    with open(test_filename1, "r") as rf:
        for line in rf.readlines():
            out_fp.write(line)
    fp = open(test_filename2, "r")
    head = next(fp)
    for line in fp:
        out_fp.write(line)

