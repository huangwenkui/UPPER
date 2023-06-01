import random
import sys
csv_file = sys.argv[1:][0]
if csv_file == "./gnomAD/00missense_gnomad_vepout.csv":
    out_file = "./LOF_GOF/randomly_selected_missense_gnomad.csv"
elif csv_file == "./gnomAD/00other_gnomad_vepout.csv":
    out_file = "./cancer_gnomad/randomly_selected_other_gnomad.csv"
csv_fp =open(csv_file,'r')
out_fp =open(out_file,'w')
lineset= set()
lines=csv_fp.readlines()
for i in range(0,20000):
    randline = random.randint(0,len(lines))
    lineset.add(randline)
    if len(lineset)>6878:
        break
fp = open(csv_file,'r')
head = next(fp)
head_arr = head.strip().split(",")
header_mapping = {el: i for i, el in enumerate(head_arr)}
out_fp.write(head)
for i,line in enumerate(fp):
    if i in lineset:
        out_fp.write(line)

