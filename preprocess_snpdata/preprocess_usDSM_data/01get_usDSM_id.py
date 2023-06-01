import sys

filename = sys.argv[1:][0]
out_filename = "./usDSM/usDSM_for_vep.txt"
out_fp = open(out_filename,"w")
map_filename = "./usDSM/usDSM_labelmap.txt"
map_fp = open(map_filename,"w")
web_filename ="./usDSM/usDSM_web.txt"
web_fp = open(web_filename,"w")
fp = open(filename,"r")
head = next(fp)
head_arr = head.strip().split(",")
head_mapping= {el: i for i, el in enumerate(head_arr)}
# chr10_14965046_A_C
# 5   140532    140532    T/C   +
for line in fp:
    line_arr = line.strip().split(",")
    chr = line_arr[1]
    pos= line_arr [2]
    alt = line_arr[3]+"/"+line_arr[4]
    keyid_arr = [chr, pos, line_arr[3], line_arr[4]]
    keyid="_".join(keyid_arr)
    label = line_arr[0]
    ad = "+"
    out= [chr,pos,pos,alt,ad]
    l= "\t".join(out)
    out_fp.write(l)
    out_fp.write("\n")

    map = [keyid,label]
    m="\t".join(map)
    map_fp.write(m)
    map_fp.write("\n")

    id ="."
    web = [chr,pos,id,line_arr[3], line_arr[4]]
    w = "\t".join(web)
    web_fp.write(w)
    web_fp.write("\n")










