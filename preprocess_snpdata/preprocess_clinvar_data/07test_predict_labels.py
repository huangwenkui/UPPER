import sys
import os
import numpy as np


def make_key_id(head_mapping, arr):
    l = [arr[i].strip("chr") for i in
         [head_mapping["CHROM"], head_mapping["Nuc-Pos"], head_mapping["REF-Nuc"], head_mapping["ALT-Nuc"]]]
    key_id = "_".join(l)
    return key_id


def std_label(labels):
    label_arr = labels.strip().split("&")
    if len(label_arr)>=1 :
        for el in label_arr:
            if el in pre_label_mapping.keys():
                label = pre_label_mapping[el]
                break
            else:
                label = "0"
    else:
        label = "0"
    return str(label)


def std_label_Polyphen2(labels):
    label_arr = labels.strip().split("&")
    if len(label_arr)>=1 :
        for el in label_arr:
            if el in pre_label_mapping_Polyphen2.keys():
                label = pre_label_mapping_Polyphen2[el]
                break
            else:
                label = "0"
    else:
        label = "0"
    return str(label)

def std_score(scores):
    score_arr = scores.strip().split("&")
    e_arr = []
    for x in score_arr:
        if x != "" and x != "." and x != "-": e_arr.append(x)
    if len(e_arr) >= 2:
        x = np.mean(list(map(float, e_arr)))
        score = x
    elif len(e_arr) == 1:
        score = e_arr[0]
    else:
        score = "0.5"
    return str(score)


test_mode = sys.argv[1:][1]
label_mapping = {'Likely_pathogenic':'1', 'Likely_benign':'0', 'Pathogenic':'1', 'Benign':'0', 'Pathogenic/Likely_pathogenic':'1','Benign/Likely_benign':'0','-1':'0','1':'1',"0":"0","Possibly pathogenic":"1","Likely Pathogenic":"1"}
pre_label_mapping = {"D": "1", "T": "0", "U":"0", "N":"0","H":"1","M":"1","L":"0","A":"1","P":"0","B":"0"}
pre_label_mapping_Polyphen2 = {"D": "1","P":"1","B":"0"}
# Polyphen2 Need to be considered separately, because "P" is "possibly damaging".the other "P" is the "polymorphism"

filename = sys.argv[1:][0]
os.makedirs("04data_predicted_labels", exist_ok=True)
basename = os.path.basename(filename)
out_filename = "04data_predicted_labels/" + basename
print("[SAVE]", out_filename)
fp = open("04data_predicted_labels/" + basename, "w")
for i, l in enumerate(open(filename)):
    header_line = False
    arr = l.strip().split(",")
    if i == 0:
        header_line = True
        header_arr = arr
        header_mapping={el:i for i,el in enumerate(header_arr)}

        if test_mode == "missense":
            new_header = ['True Label', 'key_id', 'BayesDel_addAF', 'CADD', 'ClinPred', 'DANN', 'DEOGEN2', 'FATHMM',
                          'LIST_S2', 'M_CAP', 'MPC', 'MVP', 'MetaRNN', 'MetaSVM', 'MutationAssessor', 'MutationTaster',
                          'PROVEAN', 'Polyphen2', 'PrimateAI', 'REVEL', 'SIFT4G', 'GenoCanyon','LRT','GERP++','phyloP30way_mammalian','phyloP100way_vertebrate']
        if test_mode == "other_than_missense":
            new_header = ['True Label', 'key_id', 'BayesDel_addAF', 'CADD', 'DANN',
                           'MutationTaster','GenoCanyon']
        fp.write(",".join(new_header))
        fp.write("\n")
    else:
        True_label = label_mapping[arr[header_mapping['True Label']]]
        key_id = make_key_id(header_mapping,arr)
        BayesDel_addAF = std_label(arr[header_mapping['BayesDel_addAF_pred']])
        CADD = std_score(arr[header_mapping['CADD']])
        DANN = std_score(arr[header_mapping['DANN_score']])
        MutationTaster = std_label(arr[header_mapping['MutationTaster_pred']])
        GenoCanyon = std_score(arr[header_mapping['GenoCanyon_score']])
        if test_mode == "missense":
            LRT = std_label(arr[header_mapping['LRT_pred']])
            ClinPred = std_label(arr[header_mapping['ClinPred_pred']])
            DEOGEN2 = std_label(arr[header_mapping['DEOGEN2_pred']])
            FATHMM = std_label(arr[header_mapping['FATHMM_pred']])
            LIST_S2 = std_label(arr[header_mapping['LIST_S2_pred']])
            M_CAP = std_label(arr[header_mapping['M_CAP_pred']])
            MPC = std_score(arr[header_mapping['MPC_score']])
            MVP = std_score(arr[header_mapping['MVP_score']])
            MetaRNN = std_label(arr[header_mapping['MetaRNN_pred']])
            MetaSVM = std_label(arr[header_mapping['MetaSVM_pred']])
            MutationAssessor = std_label(arr[header_mapping['MutationAssessor_pred']])
            PROVEAN = std_label(arr[header_mapping['PROVEAN_pred']])
            Polyphen2 = std_label_Polyphen2(arr[header_mapping['Polyphen2_pred']])
            PrimateAI = std_label(arr[header_mapping['PrimateAI_pred']])
            REVEL = std_score(arr[header_mapping['REVEL_score']])
            SIFT4G = std_label(arr[header_mapping['SIFT4G_pred']])
            LRT = std_score(arr[header_mapping['LRT']])
            GERP = std_score(arr[header_mapping['GERP++']])
            phyloP30way_mammalian = std_score(arr[header_mapping['phyloP30way_mammalian']])
            phyloP100way_vertebrate = std_score(arr[header_mapping['phyloP100way_vertebrate']])

        if test_mode == "missense":
            out = [True_label, key_id, BayesDel_addAF, CADD, ClinPred, DANN, DEOGEN2, FATHMM, LIST_S2,
                   M_CAP, MPC, MVP, MetaRNN, MetaSVM, MutationAssessor, MutationTaster,
                   PROVEAN, Polyphen2, PrimateAI, REVEL, SIFT4G, GenoCanyon,LRT,GERP,phyloP30way_mammalian,phyloP100way_vertebrate]

        if test_mode == "other_than_missense":
            out = [True_label, key_id, BayesDel_addAF, CADD, DANN, MutationTaster,GenoCanyon]
        fp.write(",".join(out))
        fp.write("\n")