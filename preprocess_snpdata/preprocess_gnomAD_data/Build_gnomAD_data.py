import os
import sys

if len(sys.argv[1:])==2:
    test_filename1 = sys.argv[1:][0]
    test_filename2 = sys.argv[1:][1]
    if test_filename1 == "./PTEN/PTEN_vepout.csv":
        out_filename = "./PTEN/00gnomAD_with_PTEN_missense.csv"
    elif test_filename1 == "./cancer_gnomad/cancer_vepout.csv":
        out_filename = "./cancer_gnomad/cancer_discover_vepout.csv"
    out_fp = open(out_filename, "w")
    with open(test_filename1, "r") as rf:
        for line in rf.readlines():
            out_fp.write(line)
    fp = open(test_filename2, "r")
    head = next(fp)
    for line in fp:
        out_fp.write(line)
elif len(sys.argv[1:])>2:
    test_filenames = sys.argv[1:]
    test_filename1 = sys.argv[1:][0]
    out_filename = "./cancer_gnomad/cancer_gnomAD.csv"
    out_fp = open(out_filename, "w")
    with open(test_filename1, "r") as rf:
        for line in rf.readlines():
            out_fp.write(line)
    for i,filename in enumerate(test_filenames):
        if i==0:
            continue
        else:
            fp = open(filename, "r")
            head = next(fp)
            for line in fp:
                out_fp.write(line)
