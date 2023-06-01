
filename = "./TP53/UMD_variants_US.tsv"
out_filename = "./TP53/variants_map.txt"
out_filename_forvep = "./TP53/variants_vep.txt"
out_fp = open(out_filename,'w')
out_fp_vep = open(out_filename_forvep,'w')
fp = open(filename,'r')

for i,line in enumerate(fp):
    if i==0:
        head = line
        head_arr = head.strip().split("\t")
        head_mapping = {el: i for i, el in enumerate(head_arr)}
        print(head_mapping)
        continue
    arr =line.strip().split("\t")
    HG19_Variant_chr = arr[head_mapping['HG19_Variant']].strip('chr').split(":")[0]
    Pathogenicity = arr[head_mapping['Pathogenicity']]
    if Pathogenicity=="VUS"or Pathogenicity=="#N/A":
        continue
    pos1= arr[head_mapping['HG19_Start']]
    pos2 = arr[head_mapping['HG19_End']]
    if pos2!=pos1:
        continue
    ref = arr[head_mapping['Genome_base_coding']]
    alt = arr[head_mapping['Mutant_Allele']]
    if ref=="?" or len(ref)!=1 or len(alt)!=1:
        continue
    nuc = ref + "/" + alt
    ad = "+"
    out = [HG19_Variant_chr, pos1, pos2, nuc, ad]
    l = "\t".join(out)
    out_fp_vep.write(l)
    out_fp_vep.write("\n")

    key_id_arr = [HG19_Variant_chr,pos1,ref,alt]
    key_id = "_".join(key_id_arr)
    label_mapping = [key_id,Pathogenicity]
    m = "\t".join(label_mapping)
    out_fp.write(m)
    out_fp.write("\n")

