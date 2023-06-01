import sys

train_filename = sys.argv[1:][0]
if train_filename == "./clinvar/clinvar_20220620/00clinvar_2022_synonymous.csv":
    outfilename = "./usDSM/train_std.txt"
out_fp = open(outfilename,'w')
fp = open(train_filename,'r')
head = next(fp)
head_arr = head.split(",")
head_mapping = {el:i for i, el in enumerate(head_arr)}
print(head_mapping)
for line in fp:
    line_arr = line.strip().split(",")
    chr = line_arr[head_mapping["CHROM"]]
    pos = line_arr[head_mapping["Nuc-Pos"]]
    id = "."
    ref = line_arr[head_mapping["REF-Nuc"]]
    alt = line_arr[head_mapping["ALT-Nuc"]]
    web = [chr, pos, id, ref, alt]
    w = "\t".join(web)
    out_fp.write(w)
    out_fp.write("\n")
