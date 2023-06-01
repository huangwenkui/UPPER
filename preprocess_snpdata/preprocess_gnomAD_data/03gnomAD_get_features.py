import sys
import os

filename = sys.argv[1:][0]
header = None
if filename == "./clinvar/clinvar_20220620/00clinvar_20220620_selected.csv":
    out_filename = "./clinvar/clinvar_20220620/01clinvar_20220620_selected_getfeature.csv"


test_mode = sys.argv[1:][1]
if test_mode == "missense":
    if filename == "./clinvar/clinvar_20230326/00clinvar_20230326_test.csv":
        out_filename = "./clinvar/clinvar_20230326/01clinvar_20230326_test_getfeature.csv"
elif test_mode == "other_than_missense":
    if filename == "./gnomAD/00ExAC_for_other_than_missense_test.csv":
        out_filename = "./gnomAD/01ExAC_for_other_than_missense_getfeature.csv"
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
    index_key.append(header.index('Consequence'))
    index_key.append(header.index('IMPACT'))

    index_feature = []
    if test_mode == "missense":
        index_feature.append(header.index('BayesDel_addAF_score'))
        index_feature.append(header.index('CADD'))
        index_feature.append(header.index('ClinPred_score'))
        index_feature.append(header.index('DANN_score'))
        index_feature.append(header.index('DEOGEN2_score'))
        index_feature.append(header.index('FATHMM_score'))
        index_feature.append(header.index('LIST_S2_score'))
        index_feature.append(header.index('LRT'))
        index_feature.append(header.index('M_CAP_score'))
        index_feature.append(header.index('MPC_score'))
        index_feature.append(header.index('MVP_score'))
        index_feature.append(header.index('MetaRNN_score'))
        index_feature.append(header.index('MetaSVM_score'))
        index_feature.append(header.index('MutationAssessor'))
        index_feature.append(header.index('MutationTaster'))
        index_feature.append(header.index('PROVEAN_score'))
        index_feature.append(header.index('Polyphen2'))
        index_feature.append(header.index('PrimateAI_score'))
        index_feature.append(header.index('REVEL_score'))
        index_feature.append(header.index('SIFT'))
        index_feature.append(header.index('GERP++'))
        index_feature.append(header.index('GenoCanyon_score'))
        index_feature.append(header.index('SIFT4G_score'))
        index_feature.append(header.index('phyloP30way_mammalian'))
        index_feature.append(header.index('phyloP100way_vertebrate'))
        index_feature.append(header.index('ClinVar_preferred_disease_name_in_CLNDISDB'))
    elif test_mode == "other_than_missense":
        index_feature.append(header.index('BayesDel_addAF_score'))
        index_feature.append(header.index('CADD'))
        index_feature.append(header.index('DANN_score'))
        index_feature.append(header.index('MutationTaster'))
        index_feature.append(header.index('GERP++'))
        index_feature.append(header.index('GenoCanyon_score'))
        index_feature.append(header.index('phyloP30way_mammalian'))
        index_feature.append(header.index('phyloP100way_vertebrate'))
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
