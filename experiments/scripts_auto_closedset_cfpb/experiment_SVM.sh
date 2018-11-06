#!/bin/sh

../../bin/verify.py config_SVM_32_fold1.py database_SVM_32_fold1.py
rm -rf results/closedset_cfpb/SVM/32/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/32/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_32_fold2.py database_SVM_32_fold2.py
rm -rf results/closedset_cfpb/SVM/32/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/32/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_64_fold1.py database_SVM_64_fold1.py
rm -rf results/closedset_cfpb/SVM/64/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/64/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_64_fold2.py database_SVM_64_fold2.py
rm -rf results/closedset_cfpb/SVM/64/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/64/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_128_fold1.py database_SVM_128_fold1.py
rm -rf results/closedset_cfpb/SVM/128/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/128/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_128_fold2.py database_SVM_128_fold2.py
rm -rf results/closedset_cfpb/SVM/128/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/SVM/128/fold_2/temp/subdirectory/preprocessed/
../../bin/verify.py config_SVM_128_fold3.py database_SVM_128_fold3.py