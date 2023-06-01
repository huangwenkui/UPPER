#!/bin/bash
# add --save when you want to save the experiment log
# ./run_class.sh 1 train_clinvar_2022_all_test_clinvar_20230326 TransE --save --rel_update
# ./run_class.sh 1 train_clinvar_2022_all_test_cancer_discover TransE --save --rel_update
# ./run_class.sh 1 train_clinvar_2022_all_test_PPARG TransE --save --rel_update
# ./run_class.sh 1 train_clinvar_2022_all_test_TP53 TransE --save --rel_update
# ./run_class.sh 1 train_clinvar_2022_all_test_LOFGOF_with_gnomAD TransE --save --rel_update
# ./run_class.sh 1 train_LOFGOF_train_test_LOFGOF_test TransE --save --rel_update
# ./run_class.sh 1 train_clinvar_2022_all_test_clinvar_2023other_than_missense TransE --save --rel_update
# ./run_class.sh 1 train_clinvar_2022_all_test_usDSM TransE --save --rel_update
# KGE method: TransE, RotatE, DistMult, QuatE...

GPU=$1
DATASET=$2
MODEL=$3
ARGS="$4 $5 $6 $7"
LR=(0.01)
SEED=(12306)

if [ ${DATASET} == "train_clinvar_2022_all_test_clinvar_20230326" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_all_test_clinvar_2023other_than_missense" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_all_test_LOFGOF_with_gnomAD" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_all_test_cancer_discover" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_LOFGOF_train_test_LOFGOF_test" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_all_test_TP53" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_synonymous_test_usDSM" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_all_test_usDSM" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
elif [ ${DATASET} == "train_clinvar_2022_all_test_PPARG" ]
then
    DIM=(128)
    ALPHA=(0.23)
    LAYER=(2)
fi

for alpha in "${ALPHA[@]}"
do
    for layer in "${LAYER[@]}"
    do
        for dim in "${DIM[@]}"
        do
            for lr in "${LR[@]}"
            do
                for seed in "${SEED[@]}"
                do
                    option="--dataset ${DATASET} --dim ${dim} --mode ${MODEL} --learning_rate ${lr}
                            --alpha ${alpha} --beta ${alpha} --layer ${layer} --rel_update
                            --epochs 1000 --randomseed ${seed} ${ARGS}"
                    cmd="CUDA_VISIBLE_DEVICES=${GPU} python train_class.py ${option}"
                    echo $cmd
                    eval $cmd
                done
            done
        done
    done
done