import sys

filename = sys.argv[1:][0]
out_filename = "./cancer_gnomad/discover_for_vep.txt"
out_fp = open(out_filename,"w")
fp = open(filename,"r")
head = next(fp)
head_arr = head.strip().split(",")
head_mapping= {el: i for i, el in enumerate(head_arr)}
# chr10_14965046_A_C
# 5   140532    140532    T/C   +
for line in fp:
    line_arr = line.strip().split(",")
    id = line_arr[head_mapping["var_id"]].strip().split("_")
    chr = id[0].strip("chr")
    pos1= id [1]
    pos2 = id [1]
    alt = id[2]+"/"+id[3]
    label = line_arr[head_mapping["target"]]
    if label=="1":
        continue
    # chr = line_arr[head_mapping["chr"]]
    # if chr == "":
    #     continue
    # pos = line_arr[head_mapping["pos"]]
    # ref = line_arr[head_mapping["ref"]]
    # alt = line_arr[head_mapping["alt"]]
    # r = ref+"/"+alt
    ad = "+"
    out= [chr,pos1,pos2,alt,ad]
    l= "\t".join(out)
    out_fp.write(l)
    out_fp.write("\n")


