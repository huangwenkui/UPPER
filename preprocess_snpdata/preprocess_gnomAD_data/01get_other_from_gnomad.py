import vcf
import sys
import os
STRAND_map = {"1":"+","-1":"-"}

vcf_filename = sys.argv[1:][0]
test_mode = sys.argv[1:][1]
if test_mode == "missense":
    if vcf_filename == "./gnomAD/ExAC_selected.vcf":
        vcf_outfilename = "./gnomAD/missense_gnomad_for_vep.txt"
elif test_mode == "other_than_missense":
    if vcf_filename == "./gnomAD/ExAC_selected.vcf":
        vcf_outfilename = "./gnomAD/other_gnomad_for_vep.txt"
vcf_reader = vcf.Reader(open(vcf_filename, 'r'))
fp = open(vcf_outfilename, 'w')

CSQ_format= "Allele|Consequence|IMPACT|SYMBOL|Gene|Feature_type|Feature|BIOTYPE|EXON|INTRON|HGVSc|HGVSp|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|ALLELE_NUM|DISTANCE|STRAND|FLAGS|VARIANT_CLASS|MINIMISED|SYMBOL_SOURCE|HGNC_ID|CANONICAL|TSL|APPRIS|CCDS|ENSP|SWISSPROT|TREMBL|UNIPARC|GENE_PHENO|SIFT|PolyPhen|DOMAINS|HGVS_OFFSET|GMAF|AFR_MAF|AMR_MAF|EAS_MAF|EUR_MAF|SAS_MAF|AA_MAF|EA_MAF|ExAC_MAF|ExAC_Adj_MAF|ExAC_AFR_MAF|ExAC_AMR_MAF|ExAC_EAS_MAF|ExAC_FIN_MAF|ExAC_NFE_MAF|ExAC_OTH_MAF|ExAC_SAS_MAF|CLIN_SIG|SOMATIC|PHENO|PUBMED|MOTIF_NAME|MOTIF_POS|HIGH_INF_POS|MOTIF_SCORE_CHANGE|LoF|LoF_filter|LoF_flags|LoF_info|context|ancestral"
CSQ_format_arr = CSQ_format.strip().split("|")
CSQ_format_arr_mapping = {el:i for i,el in enumerate(CSQ_format_arr)}

for reader in vcf_reader:
    csq = reader.INFO['CSQ'][0]
    CSQ_arr = csq.strip().split("|")
    Consequence = CSQ_arr[CSQ_format_arr_mapping['Consequence']]
    Consequence_arr = Consequence.strip().split("&")
    if test_mode == "missense":
        if 'missense_variant' not in Consequence_arr:
            continue
    elif test_mode == "other_than_missense":
        if 'missense_variant' in Consequence_arr or 'synonymous_variant' in Consequence_arr:
            continue
    try:
        STRAND = STRAND_map[CSQ_arr[CSQ_format_arr_mapping['STRAND']]]
    except:
        continue
    CHROM = reader.CHROM
    Nuc_Pos = str(reader.POS)
    REF_Nuc = reader.REF
    ALT_Nuc = str(reader.ALT[0])
    if len(REF_Nuc)>1:
        continue
    if len(ALT_Nuc)>1:
        continue
    nuc = REF_Nuc + "/" + ALT_Nuc
    out = [CHROM, Nuc_Pos, Nuc_Pos, nuc, STRAND]
    l = "\t".join(out)
    fp.write(l)
    fp.write("\n")

