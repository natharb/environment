#!/bin/sh

../../bin/verify.py config_SVM_256_fold1.py database_SVM_256_fold1.py
rm -rf results/closedset_cfpb/SVM/256/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/256/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_256_fold2.py database_SVM_256_fold2.py
rm -rf results/closedset_cfpb/SVM/256/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/256/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_512_fold1.py database_SVM_512_fold1.py
rm -rf results/closedset_cfpb/SVM/512/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/512/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_512_fold2.py database_SVM_512_fold2.py
rm -rf results/closedset_cfpb/SVM/512/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/512/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_1024_fold1.py database_SVM_1024_fold1.py
rm -rf results/closedset_cfpb/SVM/1024/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/1024/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_1024_fold2.py database_SVM_1024_fold2.py
rm -rf results/closedset_cfpb/SVM/1024/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/1024/fold_2/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_1024_fold3.py database_SVM_1024_fold3.py

../../bin/verify.py config_SVM_2048_fold1.py database_SVM_2048_fold1.py
rm -rf results/closedset_cfpb/SVM/2048/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/2048/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_2048_fold2.py database_SVM_2048_fold2.py
rm -rf results/closedset_cfpb/SVM/2048/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/2048/fold_2/temp/subdirectory/preprocessed/