import sys
import os


filename = sys.argv[1:][0]
out_filename = "./TP53/TP53_for_vep.tsv"
out_fp = open(out_filename,"w")
map_filename = "./TP53/TP53_labelmap.txt"
map_fp = open(map_filename,"w")

fp = open(filename,"r")
# head = next(fp)
# head_arr = head.strip().split(",")
# head_mapping= {el: i for i, el in enumerate(head_arr)}
# chr10_14965046_A_C
# 5   140532    140532    T/C   +
for line in fp:
    line_arr = line.strip().split()
    chr = line_arr[1].strip("chr")
    pos = line_arr[2]
    alt = line_arr[4]+"/"+line_arr[5]
    keyid_arr = [chr, pos, line_arr[4], line_arr[5]]
    keyid="_".join(keyid_arr)
    label = line_arr[7]
    ad = "+"
    out= [chr,pos,pos,alt,ad]
    l= "\t".join(out)
    out_fp.write(l)
    out_fp.write("\n")

    map = [keyid,label]
    m="\t".join(map)
    map_fp.write(m)
    map_fp.write("\n")











