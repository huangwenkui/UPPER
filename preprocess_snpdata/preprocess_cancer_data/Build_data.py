import os
import sys

if len(sys.argv[1:])==2:
    test_filename1 = sys.argv[1:][0]
    test_filename2 = sys.argv[1:][1]
    if test_filename1 == "./cancer_gnomad/cancer_vepout.csv":
        out_filename = "./cancer_gnomad/cancer_discover_vepout.csv"
    out_fp = open(out_filename, "w")
    with open(test_filename1, "r") as rf:
        for line in rf.readlines():
            out_fp.write(line)
    fp = open(test_filename2, "r")
    head = next(fp)
    for line in fp:
        out_fp.write(line)

