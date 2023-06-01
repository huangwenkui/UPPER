import sys
import os

filename = sys.argv[1:][0]
test_mode = sys.argv[1:][1]
if test_mode == "missense":
    if filename == "./clinvar/clinvar_20220620/00clinvar_20220620_selected.csv":
        out_filename = "./clinvar/clinvar_20220620/01clinvar_20220620_selected_getfeature.csv"
    if filename == "./clinvar/clinvar_20230326/00clinvar_20230326_test.csv":
        out_filename = "./clinvar/clinvar_20230326/01clinvar_20230326_test_getfeature.csv"
elif test_mode == "other_than_missense":
    if filename == "./clinvar/clinvar_20230326/00clinvar_2023other_than_missense_gnomAD_test.csv":
        out_filename = "./clinvar/clinvar_20230326/01clinvar_2023other_than_missense_test_getfeature.csv"
    if filename == "./clinvar/clinvar_20220620/00clinvar_2022other_than_missense_selected.csv":
        out_filename = "./clinvar/clinvar_20220620//01clinvar_2022other_than_missense_test_getfeature.csv"


fp = open(out_filename, "w")
for i, l in enumerate(open(filename)):
    header_line = False
    arr = l.strip().split(",")
    if i == 0:
        header_line = True
        header = arr
    index_label = [header.index('True Label')]
    index_id = []
    index_id.append(header.index('CHROM'))
    index_id.append(header.index('Nuc-Pos'))
    index_id.append(header.index('REF-Nuc'))
    index_id.append(header.index('ALT-Nuc'))

    index_key = []
    index_key.append(header.index('Ensembl-Gene-ID'))
    index_key.append(header.index('Ensembl-Protein-ID'))
    index_key.append(header.index('Ensembl-Transcript-ID'))
    index_key.append(header.index('Uniprot-Accession'))
    index_key.append(header.index('Amino_acids'))
    index_key.append(header.index('cDNA_position'))
    index_key.append(header.index('CDS_position'))
    index_key.append(header.index('Protein_position'))
    index_key.append(header.index('Codons'))
    index_key.append(header.index('DOMAINS'))
    index_key.append(header.index('Consequence'))
    index_key.append(header.index('IMPACT'))
    index_key.append(header.index('kGp3_AF'))
    index_key.append(header.index('ExAC_AF'))
    index_key.append(header.index('gnomAD_exomes_AF'))

    index_feature = []
    if test_mode == "missense":
        index_feature.append(header.index('BayesDel_addAF_rankscore'))
        index_feature.append(header.index('BayesDel_noAF_rankscore'))
        index_feature.append(header.index('CADD_raw_rankscore'))
        index_feature.append(header.index('CADD_raw_rankscore_hg19'))
        index_feature.append(header.index('ClinPred_rankscore'))
        index_feature.append(header.index('DANN_rankscore'))
        index_feature.append(header.index('DEOGEN2_rankscore'))
        index_feature.append(header.index('Eigen_PC_raw_coding_rankscore'))
        index_feature.append(header.index('Eigen_raw_coding_rankscore'))
        index_feature.append(header.index('FATHMM_converted_rankscore'))
        index_feature.append(header.index('LIST_S2_rankscore'))
        index_feature.append(header.index('M_CAP_rankscore'))
        index_feature.append(header.index('MPC_rankscore'))
        index_feature.append(header.index('MVP_rankscore'))
        index_feature.append(header.index('MetaLR_rankscore'))
        index_feature.append(header.index('MetaRNN_rankscore'))
        index_feature.append(header.index('MetaSVM_rankscore'))
        index_feature.append(header.index('MutPred_rankscore'))
        index_feature.append(header.index('MutationAssessor_rankscore'))
        index_feature.append(header.index('MutationTaster_converted_rankscore'))
        index_feature.append(header.index('PROVEAN_converted_rankscore'))
        index_feature.append(header.index('Polyphen2_HDIV_rankscore'))
        index_feature.append(header.index('Polyphen2_HVAR_rankscore'))
        index_feature.append(header.index('PrimateAI_rankscore'))
        index_feature.append(header.index('REVEL_rankscore'))
        index_feature.append(header.index('SIFT4G_converted_rankscore'))
        index_feature.append(header.index('SIFT_converted_rankscore'))
        index_feature.append(header.index('VEST4_rankscore'))
        index_feature.append(header.index('fathmm_MKL_coding_rankscore'))
        index_feature.append(header.index('fathmm_XF_coding_rankscore'))
        index_feature.append(header.index('phastCons100way_vertebrate_rankscore'))
        index_feature.append(header.index('phyloP100way_vertebrate_rankscore'))
        index_feature.append(header.index('ClinVar_preferred_disease_name_in_CLNDISDB'))
    elif test_mode == "other_than_missense":
        index_feature.append(header.index('BayesDel_addAF_rankscore'))
        index_feature.append(header.index('BayesDel_noAF_rankscore'))
        index_feature.append(header.index('CADD_raw_rankscore'))
        index_feature.append(header.index('CADD_raw_rankscore_hg19'))
        index_feature.append(header.index('DANN_rankscore'))
        index_feature.append(header.index('Eigen_PC_raw_coding_rankscore'))
        index_feature.append(header.index('Eigen_raw_coding_rankscore'))
        index_feature.append(header.index('MutationTaster_converted_rankscore'))
        index_feature.append(header.index('VEST4_rankscore'))
        index_feature.append(header.index('fathmm_MKL_coding_rankscore'))
        index_feature.append(header.index('fathmm_XF_coding_rankscore'))
        index_feature.append(header.index('phastCons100way_vertebrate_rankscore'))
        index_feature.append(header.index('phyloP100way_vertebrate_rankscore'))
        index_feature.append(header.index('ClinVar_preferred_disease_name_in_CLNDISDB'))

    label = [arr[idx] for idx in index_label]
    ids = [arr[idx] for idx in index_id]
    key = [arr[idx] for idx in index_key]
    feature = [arr[idx] for idx in index_feature]

    out = label + ids + key + feature
    if not header_line:
        out = [el if el != " " else "." for el in out]
    fp.write(",".join(out))
    fp.write("\n")
