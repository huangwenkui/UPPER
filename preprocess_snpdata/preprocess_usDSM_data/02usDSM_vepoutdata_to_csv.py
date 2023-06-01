import vcf
import sys
import os


def make_key_id(CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc):
    l = [CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc]
    key_id = "_".join(l)
    return key_id

map_file = "./usDSM/usDSM_labelmap.txt"
mp_fp = open(map_file,"r")
label_map = {}
for line in mp_fp:
    line_arr = line.strip().split("\t")
    id = line_arr[0]
    label = line_arr[1]
    label_map[id]=label
cadd_file ="./usDSM/cadd_result.tsv"
cadd_fp =open(cadd_file,"r")
cadd_mapping ={}
for line in cadd_fp:
    line_arr = line.strip().split("\t")
    chr = line_arr[0]
    Nuc_Pos = line_arr[1]
    REF_Nuc = line_arr[2]
    ALT_Nuc = line_arr[3]
    key_id = make_key_id(chr, Nuc_Pos, REF_Nuc, ALT_Nuc)
    score = line_arr[4]
    cadd_mapping[key_id]=score

PrDSM_file ="./usDSM/PrDSM_result.vcf"
PrDSM_fp = open(PrDSM_file, 'r')
head = next(PrDSM_fp)
head_arr = head.strip().split()
header_mapping = {el: i for i, el in enumerate(head_arr)}
TraP_mapping ={}
SilVA_mapping ={}
FATHMM_MKL_mapping ={}
PrDSM_mapping ={}
for reader in PrDSM_fp:
    p_reader = reader.strip().split()
    chr = p_reader[header_mapping["Chr"]]
    Pos = p_reader[header_mapping["Pos"]]
    Ref = p_reader[header_mapping["Ref"]]
    Alt = p_reader[header_mapping["Alt"]]
    key_id = make_key_id(chr, Pos, Ref, Alt)
    TraP = p_reader[header_mapping["TraP"]]
    SilVA = p_reader[header_mapping["SilVA"]]
    FATHMM_MKL = p_reader[header_mapping["FATHMM-MKL"]]
    PrDSM = p_reader[header_mapping["PrDSM"]]
    TraP_mapping[key_id] = TraP
    SilVA_mapping[key_id] = SilVA
    FATHMM_MKL_mapping[key_id] = FATHMM_MKL
    PrDSM_mapping[key_id] = PrDSM


vcf_filename = sys.argv[1:][0]
if vcf_filename == "./usDSM/usDSM_vepout.vcf":
    vcf_outfilename = "./usDSM/usDSM_vepout.csv"

vcf_reader = vcf.Reader(open(vcf_filename, 'r'))
test_mode = sys.argv[1:][1]


print(vcf_outfilename)
fp = open(vcf_outfilename, 'w')
# Record(CHROM=1, POS=13418, REF=G, ALT=[GAGAG])

# {'CSQ': ['GAGAGAGA|downstream_gene_variant|MODIFIER|WASH7P|653635|Transcript|NR_024540.1|transcribed_pseudogene|||||||||||941|-1||EntrezGene|||rseq_mrna_match||GAGA|GAGA|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
# Format: Allele|Consequence|IMPACT|SYMBOL|Gene|Feature_type|Feature|BIOTYPE|EXON|INTRON|HGVSc|HGVSp|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|DISTANCE|STRAND|FLAGS|SYMBOL_SOURCE|HGNC_ID|ENSP|REFSEQ_MATCH|REFSEQ_OFFSET|GIVEN_REF|USED_REF|BAM_EDIT|GENE_PHENO|BayesDel_addAF_pred|BayesDel_addAF_score|CADD_phred|CADD_raw|ClinPred_pred|ClinPred_score|DANN_score|DEOGEN2_pred|DEOGEN2_score|Ensembl_geneid|Ensembl_proteinid|Ensembl_transcriptid|FATHMM_pred|FATHMM_score|GERP++_NR|GERP++_RS|GenoCanyon_score|LIST-S2_pred|LIST-S2_score|LRT_pred|LRT_score|M-CAP_pred|M-CAP_score|MPC_score|MVP_score|MetaRNN_pred|MetaRNN_score|MetaSVM_pred|MetaSVM_score|MutPred_score|MutationAssessor_pred|MutationAssessor_score|MutationTaster_pred|MutationTaster_score|PROVEAN_pred|PROVEAN_score|Polyphen2_HDIV_pred|Polyphen2_HDIV_score|PrimateAI_pred|PrimateAI_score|REVEL_score|SIFT4G_pred|SIFT4G_score|SIFT_pred|SIFT_score|Uniprot_acc|alt|chr|clinvar_MedGen_id|clinvar_OMIM_id|clinvar_Orphanet_id|clinvar_clnsig|clinvar_hgvs|clinvar_trait|clinvar_var_source|genename|phyloP30way_mammalian|ref|rs_dbSNP">
pathogenicity_mapping = {'Deleterious':'1', 'Likely_benign':'-1', 'Pathogenic':'1', 'Benign':'-1', 'Pathogenic/Likely_pathogenic':'1','Benign/Likely_benign':'-1'}

CSQ_format="Allele|Consequence|IMPACT|SYMBOL|Gene|Feature_type|Feature|BIOTYPE|EXON|INTRON|HGVSc|HGVSp|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|DISTANCE|STRAND|FLAGS|SYMBOL_SOURCE|HGNC_ID|ENSP|GENE_PHENO|DOMAINS|1000Gp3_AF|BayesDel_addAF_pred|BayesDel_addAF_rankscore|BayesDel_noAF_pred|BayesDel_noAF_rankscore|CADD_phred|CADD_phred_hg19|CADD_raw_rankscore|CADD_raw_rankscore_hg19|ClinPred_pred|ClinPred_rankscore|DANN_rankscore|DEOGEN2_pred|DEOGEN2_rankscore|Eigen-PC-raw_coding_rankscore|Eigen-raw_coding_rankscore|Ensembl_geneid|Ensembl_proteinid|Ensembl_transcriptid|ExAC_AF|FATHMM_converted_rankscore|FATHMM_pred|GERP++_RS_rankscore|GM12878_fitCons_rankscore|GenoCanyon_rankscore|H1-hESC_fitCons_rankscore|HUVEC_fitCons_rankscore|LINSIGHT_rankscore|LIST-S2_pred|LIST-S2_rankscore|M-CAP_pred|M-CAP_rankscore|MPC_rankscore|MVP_rankscore|MetaLR_pred|MetaLR_rankscore|MetaRNN_pred|MetaRNN_rankscore|MetaSVM_pred|MetaSVM_rankscore|MutPred_rankscore|MutationAssessor_pred|MutationAssessor_rankscore|MutationTaster_converted_rankscore|MutationTaster_pred|PROVEAN_converted_rankscore|PROVEAN_pred|Polyphen2_HDIV_pred|Polyphen2_HDIV_rankscore|Polyphen2_HVAR_pred|Polyphen2_HVAR_rankscore|PrimateAI_pred|PrimateAI_rankscore|REVEL_rankscore|SIFT4G_converted_rankscore|SIFT4G_pred|SIFT_converted_rankscore|SIFT_pred|SiPhy_29way_logOdds_rankscore|Uniprot_acc|VEST4_rankscore|aaalt|aaref|alt|bStatistic_converted_rankscore|chr|clinvar_MedGen_id|clinvar_OMIM_id|clinvar_Orphanet_id|clinvar_clnsig|clinvar_hgvs|clinvar_trait|clinvar_var_source|fathmm-MKL_coding_pred|fathmm-MKL_coding_rankscore|fathmm-XF_coding_pred|fathmm-XF_coding_rankscore|genename|gnomAD_exomes_AF|integrated_fitCons_rankscore|phastCons100way_vertebrate_rankscore|phastCons30way_mammalian_rankscore|phyloP100way_vertebrate_rankscore|phyloP30way_mammalian_rankscore|ref|rs_dbSNP"
CSQ_format_arr = CSQ_format.strip().split("|")
CSQ_format_arr_mapping = {el:i for i,el in enumerate(CSQ_format_arr)}
print(CSQ_format_arr_mapping)
if test_mode == "synonymous":
    head_line = ["True Label", "CHROM", "Nuc-Pos", "REF-Nuc", "ALT-Nuc","Amino_acids", "cDNA_position","CDS_position",
                 "Protein_position","Codons","DOMAINS", "Consequence","IMPACT","BIOTYPE","kGp3_AF","ExAC_AF","gnomAD_exomes_AF",
                 "Ensembl-Gene-ID", "Ensembl-Protein-ID",
                 "Ensembl-Transcript-ID", "Uniprot-Accession","CADD_raw_rankscore",'TraP','SilVA','fathmm_MKL_coding_rankscore','PrDSM'
                 ,'ClinVar_preferred_disease_name_in_CLNDISDB']

h= ",".join(head_line)
fp.write(h)
fp.write("\n")
count = 0
for reader in vcf_reader:
    try:
        CSQ_arr = reader.INFO['CSQ'][0].strip().split("|")
    except:
        continue
    CHROM = reader.CHROM
    Nuc_Pos = str(reader.POS)
    REF_Nuc = reader.REF
    ALT_Nuc = str(reader.ALT[0])

    key_id =make_key_id(CHROM,Nuc_Pos,REF_Nuc,ALT_Nuc)
    True_Label = pathogenicity_mapping[label_map[key_id]]
    Consequence = CSQ_arr[CSQ_format_arr_mapping['Consequence']]
    Amino_acids = CSQ_arr[CSQ_format_arr_mapping['Amino_acids']]
    cDNA_position = CSQ_arr[CSQ_format_arr_mapping['cDNA_position']]
    CDS_position = CSQ_arr[CSQ_format_arr_mapping['CDS_position']]
    Protein_position = CSQ_arr[CSQ_format_arr_mapping['Protein_position']]
    Codons = CSQ_arr[CSQ_format_arr_mapping['Codons']]
    DOMAINS = CSQ_arr[CSQ_format_arr_mapping['DOMAINS']]
    IMPACT = CSQ_arr[CSQ_format_arr_mapping['IMPACT']]
    BIOTYPE = CSQ_arr[CSQ_format_arr_mapping['BIOTYPE']]
    kGp3_AF = CSQ_arr[CSQ_format_arr_mapping['1000Gp3_AF']]
    ExAC_AF = CSQ_arr[CSQ_format_arr_mapping['ExAC_AF']]
    gnomAD_exomes_AF = CSQ_arr[CSQ_format_arr_mapping['gnomAD_exomes_AF']]
    Ensembl_Gene_ID = CSQ_arr[CSQ_format_arr_mapping['Gene']]
    if Ensembl_Gene_ID=="":
        continue
    Ensembl_Protein_ID = CSQ_arr[CSQ_format_arr_mapping['ENSP']]
    Ensembl_Transcript_ID = CSQ_arr[CSQ_format_arr_mapping['Feature']]
    Uniprot_Accession = CSQ_arr[CSQ_format_arr_mapping['Uniprot_acc']]
    cadd = cadd_mapping[key_id]
    TraP = TraP_mapping[key_id]
    SilVA = SilVA_mapping[key_id]
    FATHMM_MKL = FATHMM_MKL_mapping[key_id]
    PrDSM = PrDSM_mapping[key_id]
    try:
        ClinVar_preferred_disease_name_in_CLNDISDB = reader.INFO['CLNDN'][0]
    except:
        ClinVar_preferred_disease_name_in_CLNDISDB = "not_provided"
    if test_mode == "synonymous":
        out = [True_Label, CHROM, Nuc_Pos, REF_Nuc, ALT_Nuc, Amino_acids, cDNA_position, CDS_position,
               Protein_position, Codons,
               DOMAINS, Consequence, IMPACT, BIOTYPE, kGp3_AF, ExAC_AF, gnomAD_exomes_AF,
               Ensembl_Gene_ID, Ensembl_Protein_ID, Ensembl_Transcript_ID, Uniprot_Accession,cadd, TraP,SilVA,FATHMM_MKL,PrDSM
               ,ClinVar_preferred_disease_name_in_CLNDISDB]
    # ["True Label", "CHROM", "Nuc-Pos", "REF-Nuc", "ALT-Nuc", "Ensembl-Gene-ID", "Ensembl-Protein-ID", "Ensembl-Transcript-ID", "Uniprot-Accession", 'BayesDel_addAF_score', 'BayesDel_addAF_pred', 'CADD', 'CADD_phred', 'ClinPred_score', 'ClinPred_pred', 'DANN_score', 'DEOGEN2_score', 'DEOGEN2_pred', 'FATHMM_score', 'FATHMM_pred',  'LIST_S2_score', 'LIST_S2_pred', 'LRT', 'LRT_pred', 'M_CAP_score', 'M_CAP_pred', 'MPC_score', 'MVP_score',   'MetaRNN_score', 'MetaRNN_pred', 'MetaSVM_score', 'MetaSVM_pred', 'MutationAssessor', 'MutationAssessor_pred',  'MutationTaster', 'MutationTaster_pred', 'PROVEAN_score', 'PROVEAN_pred', 'Polyphen2', 'Polyphen2_pred', 'PrimateAI_score', 'PrimateAI_pred', 'REVEL_score', 'SIFT', 'SIFT_pred', 'GERP++_NR', 'GERP++', 'GenoCanyon_score',  'SIFT4G_score', 'SIFT4G_pred', 'phyloP', 'ClinVar_preferred_disease_name_in_CLNDISDB']
    try:
        l = ",".join(out)
        count += 1
        fp.write(l)
        fp.write("\n")
    except:
        continue
print(count)