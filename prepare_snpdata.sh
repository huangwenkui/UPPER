#!/bin/sh

#_______________________reactome_kggraph________________________________
#mkdir -p reactome/
#wget https://reactome.org/download/current/interactors/reactome.homo_sapiens.interactions.tab-delimited.txt -O reactome/reactome.homo_sapiens.interactions.tab-delimited.txt
#python ./preprocess_snpdata/script/make_reactome_graph.py
#python ./preprocess_snpdata/script/preprocess_reactome.py


#____clinvar_dataset__(vep is needed to annotate snp.If you don't install vep, skip this step.Because there is an already processed dataset in ./kgdata/)_____
#wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar_20230326.vcf.gz -O ./clinvar/clinvar_20230326.vcf.gz
#gzip -d ./clinvar/clinvar_20230326.vcf.gz

#python ./preprocess_snpdata/preprocess_clinvar_data/01select_clinvardata.py ./clinvar/clinvar_20220620/clinvar_20220620.vcf missense
#python ./preprocess_snpdata/preprocess_clinvar_data/02clinvar_vepoutdata_to_csv.py ./clinvar/clinvar_20220620/clinvar_20220620_selected_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_clinvar_data/02clinvar_vepoutdata_to_csv.py ./clinvar/clinvar_20220620/clinvar_20220620_selected_vepout.vcf other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/02clinvar_vepoutdata_to_csv.py ./clinvar/clinvar_20220620/clinvar_20220620_selected_vepout.vcf synonymous
#python ./preprocess_snpdata/preprocess_clinvar_data/03clinvar_get_features.py ./clinvar/clinvar_20220620/00clinvar_20220620_selected.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/03clinvar_get_features.py ./clinvar/clinvar_20220620/00clinvar_2022other_than_missense_selected.csv other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/04clinvar_standard.py ./clinvar/clinvar_20220620/01clinvar_20220620_selected_getfeature.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/04clinvar_standard.py ./clinvar/clinvar_20220620/01clinvar_2022other_than_missense_test_getfeature.csv other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/05clinvar_desc.py ./clinvar/clinvar_20220620/02clinvar_20220620_selected_standard.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/05clinvar_desc.py ./clinvar/clinvar_20220620/02clinvar_2022other_than_missense_test_standard.csv other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/06clinvar_tograph.py ./clinvar/clinvar_20220620/03clinvar_20220620_selected_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/06clinvar_tograph.py ./clinvar/clinvar_20220620/03clinvar_2022other_than_missense_test_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/08Build_training_set.py ./03data_graph/clinvar_20220620 ./03data_graph/clinvar_2022other_than_missense


#python ./preprocess_snpdata/preprocess_clinvar_data/01select_clinvardata.py ./clinvar/clinvar_20230326/clinvar_20230326.vcf
#python ./preprocess_snpdata/preprocess_clinvar_data/02clinvar_vepoutdata_to_csv.py ./clinvar/clinvar_20230326/clinvar_20230326_selected_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_clinvar_data/02clinvar_vepoutdata_to_csv.py ./clinvar/clinvar_20230326/clinvar_20230326_selected_vepout.vcf other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/Build_the_test_set.py ./clinvar/clinvar_20230326/00clinvar_20230326_selected.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/Build_the_test_set.py ./clinvar/clinvar_20230326/00clinvar_2023other_than_missense_selected.csv other_than_missense
#python ./preprocess_snpdata/preprocess_LOFGOF_data/Build_data.py ./clinvar/clinvar_20230326/00clinvar_2023other_than_missense_test.csv ./gnomAD/00other_gnomad_vepout_value.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/03clinvar_get_features.py ./clinvar/clinvar_20230326/00clinvar_20230326_test.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/03clinvar_get_features.py ./clinvar/clinvar_20230326/00clinvar_2023other_than_missense_gnomAD_test.csv other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/04clinvar_standard.py ./clinvar/clinvar_20230326/01clinvar_20230326_test_getfeature.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/04clinvar_standard.py ./clinvar/clinvar_20230326/01clinvar_2023other_than_missense_test_getfeature.csv other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/05clinvar_desc.py ./clinvar/clinvar_20230326/02clinvar_20230326_test_standard.csv missense
#python ./preprocess_snpdata/preprocess_clinvar_data/05clinvar_desc.py ./clinvar/clinvar_20230326/02clinvar_2023other_than_missense_test_standard.csv other_than_missense
#python ./preprocess_snpdata/preprocess_clinvar_data/06clinvar_tograph.py ./clinvar/clinvar_20230326/03clinvar_20230326_test_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/06clinvar_tograph.py ./clinvar/clinvar_20230326/03clinvar_2023other_than_missense_test_desc.csv


#____usDSM_dataset__
#python ./preprocess_snpdata/preprocess_usDSM_data/00get_train_vcf.py ./clinvar/clinvar_20220620/00clinvar_2022_synonymous.csv
#python ./preprocess_snpdata/preprocess_usDSM_data/01get_usDSM_id.py ./usDSM/usDSM.csv
#python ./preprocess_snpdata/preprocess_usDSM_data/02usDSM_vepoutdata_to_csv.py ./usDSM/usDSM_vepout.vcf synonymous
#python ./preprocess_snpdata/preprocess_usDSM_data/05standard.py ./usDSM/usDSM_vepout.csv synonymous
#python ./preprocess_snpdata/preprocess_usDSM_data/05standard.py ./clinvar/clinvar_20220620/00clinvar_2022_synonymous.csv synonymous
#python ./preprocess_snpdata/preprocess_usDSM_data/06usDSM_tograph.py ./usDSM/01usDSM_standard.csv
#python ./preprocess_snpdata/preprocess_usDSM_data/06usDSM_tograph.py ./usDSM/01clinvar_2022_synonymous_standard.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/08Build_training_set.py ./03data_graph/clinvar_2022 ./03data_graph/clinvar_2022_synonymous

#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/usDSM
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_synonymous ./03data_graph/usDSM
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/clinvar_20230326
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/clinvar_2023other_than_missense


#____TP53_dataset__
#python ./preprocess_snpdata/preprocess_TP53_data/01select_data.py
#python ./preprocess_snpdata/preprocess_TP53_data/01get_id_forvep.py ./TP53/TP53.txt
#python ./preprocess_snpdata/preprocess_TP53_data/build_test_data.py ./TP53/TP53_for_vep_from_metaRNN.tsv ./TP53/TP53_for_vep.txt
#python ./preprocess_snpdata/preprocess_TP53_data/02TP53_vepoutdata_to_csv.py ./TP53/TP53_test_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_TP53_data/03get_features.py ./TP53/TP53_test_vepout.csv
#python ./preprocess_snpdata/preprocess_TP53_data/04standard.py ./TP53/01tp53_getfeature.csv
#python ./preprocess_snpdata/preprocess_TP53_data/05desc.py ./TP53/02tp53_standard.csv
#python ./preprocess_snpdata/preprocess_TP53_data/06tograph.py ./TP53/03tp53_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/TP53


#____LOF_GOF_data__

#python ./preprocess_snpdata/preprocess_LOFGOF_data/01LOFGOF_getdatamap.py ./LOF_GOF/goflof_HGMD2019.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/randomly_selected.py ./LOF_GOF/Classify_GOF_LOF_getdata.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/Classify_LOFGOF_tograph.py ./LOF_GOF/Classify_GOF_LOF_test.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/Classify_LOFGOF_tograph.py ./LOF_GOF/Classify_GOF_LOF_train.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/LOFGOF_train ./03data_graph/LOFGOF_test

#python ./preprocess_snpdata/preprocess_LOFGOF_data/02LOFGOF_vepdata_to_csv.py ./LOF_GOF/goflof_HGMD2019_map.txt ./LOF_GOF/goflof_HGMD2019_hgvsc_vepout.vcf
#python ./preprocess_snpdata/preprocess_LOFGOF_data/Build_data.py ./LOF_GOF/goflof_HGMD2019_vepout.csv ./LOF_GOF/randomly_selected_missense_gnomad.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/Build_the_test_set.py ./LOF_GOF/goflof_HGMD2019_with_gnomAD.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/03LOFGOF_get_features.py ./LOF_GOF/goflof_HGMD2019_with_gnomAD_test.csv missense
#python ./preprocess_snpdata/preprocess_LOFGOF_data/04LOFGOF_standard.py ./LOF_GOF/00goflof_HGMD2019_with_gnomAD_test_getfeature.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/05LOFGOF_desc.py ./LOF_GOF/01goflof_HGMD2019_with_gnomAD_test_standard.csv
#python ./preprocess_snpdata/preprocess_LOFGOF_data/06LOFGOF_tograph.py ./LOF_GOF/02goflof_HGMD2019_with_gnomAD_test_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/LOFGOF_with_gnomAD


#____gnomAD_dataset__
#wget https://datasetgnomad.blob.core.windows.net/dataset/legacy/exac_browser/ExAC.r1.sites.vep.vcf.gz
#gzip -d ExAC.r1.sites.vep.vcf.gz
#python ./preprocess_snpdata/preprocess_gnomAD_data/01select_gnomAD_data.py ./gnomAD/ExAC.r1.sites.vep.vcf
#python ./preprocess_snpdata/preprocess_gnomAD_data/01get_rsid.py ./gnomAD/ExAC_selected.vcf
#python ./preprocess_snpdata/preprocess_gnomAD_data/01get_other_from_gnomad.py ./gnomAD/ExAC_selected.vcf other_than_missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/01get_other_from_gnomad.py ./gnomAD/ExAC_selected.vcf missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/02gnomAD_vepoutdata_to_csv.py ./gnomAD/missense_gnomad_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/02gnomAD_vepoutdata_to_csv.py ./gnomAD/other_gnomad_vepout.vcf other_than_missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/randomly_selected.py ./gnomAD/00missense_gnomad_vepout.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/Build_the_test_set.py ./gnomAD/00ExAC_for_other_than_missense.csv other_than_missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/03gnomAD_get_features.py ./gnomAD/00ExAC_for_other_than_missense_test.csv other_than_missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/04gnomAD_standard.py ./gnomAD/01ExAC_for_other_than_missense_getfeature.csv other_than_missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/05gnomdAD_desc.py ./gnomAD/02ExAC_for_other_than_missense_standard.csv other_than_missense
#python ./preprocess_snpdata/preprocess_gnomAD_data/06gnomdAD_tograph.py ./gnomAD/03ExAC_for_other_than_missense_desc.csv

#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022 ./03data_graph/gnomAD_for_other_than_missense


#____cancer_Discover_dataset__
#python ./preprocess_snpdata/preprocess_cancer_data/merge_data.py ./cancer_gnomad/cancer_gnomad.final0302.HS.reformat.cnn.csv ./cancer_gnomad/cancer_gnomad.final0302.HIS.reformat.cnn.csv
#python ./preprocess_snpdata/preprocess_cancer_data/01get_cancer_Discover_id.py ./cancer_gnomad/cancer_Discover.csv
#python ./preprocess_snpdata/preprocess_cancer_data/02cancer_Discover_vepoutdata_to_csv.py ./cancer_gnomad/cancer_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_cancer_data/02cancer_Discover_vepoutdata_to_csv.py ./cancer_gnomad/discover_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_cancer_data/Build_data.py ./cancer_gnomad/cancer_vepout.csv ./cancer_gnomad/discover_vepout.csv
#python ./preprocess_snpdata/preprocess_cancer_data/Build_the_test_set.py ./cancer_gnomad/cancer_discover_vepout.csv missense
#python ./preprocess_snpdata/preprocess_cancer_data/03cancer_get_features.py ./cancer_gnomad/cancer_discover_test.csv missense
#python ./preprocess_snpdata/preprocess_cancer_data/04cancer_standard.py ./cancer_gnomad/01cancer_discover_test_getfeature.csv missense
#python ./preprocess_snpdata/preprocess_cancer_data/05cancer_desc.py ./cancer_gnomad/02cancer_discover_test_standard.csv missense
#python ./preprocess_snpdata/preprocess_cancer_data/06cancer_tograph.py ./cancer_gnomad/03cancer_discover_test_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/cancer_discover


#____PPAGR_dataset__
#python ./preprocess_snpdata/preprocess_PPAGR_data/01get_id_forvep.py ./PPARG/PPARG.txt
#python ./preprocess_snpdata/preprocess_PPAGR_data/02PPAGR_vepoutdata_to_csv.py ./PPARG/PPARG_vepout.vcf missense
#python ./preprocess_snpdata/preprocess_PPAGR_data/Build_the_test_set.py ./PPARG/PPARG_vepout.csv missense
#python ./preprocess_snpdata/preprocess_PPAGR_data/03PPAGR_desc.py ./PPARG/PPARG_test.csv missense
#python ./preprocess_snpdata/preprocess_PPAGR_data/04PPAGR_tograph.py ./PPARG/00PPARG_desc.csv
#python ./preprocess_snpdata/preprocess_clinvar_data/prekg_train_clinvar2022_test_clinvar2023.py ./03data_graph/clinvar_2022_all ./03data_graph/PPARG


