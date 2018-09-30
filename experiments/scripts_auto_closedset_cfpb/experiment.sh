#!/bin/sh

../../bin/verify.py config_GMM_256_fold1.py database_GMM_256_fold1.py
rm -rf results/closedset_cfpb/GMM/256/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/256/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_GMM_256_fold2.py database_GMM_256_fold2.py
rm -rf results/closedset_cfpb/GMM/256/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/256/fold_2/temp/subdirectory/preprocessed/


../../bin/verify.py config_GMM_512_fold1.py database_GMM_512_fold1.py
rm -rf results/closedset_cfpb/GMM/512/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/512/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_GMM_512_fold2.py database_GMM_512_fold2.py
rm -rf results/closedset_cfpb/GMM/512/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/512/fold_2/temp/subdirectory/preprocessed/


../../bin/verify.py config_GMM_1024_fold1.py database_GMM_1024_fold1.py
rm -rf results/closedset_cfpb/GMM/1024/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/1024/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_GMM_1024_fold2.py database_GMM_1024_fold2.py
rm -rf results/closedset_cfpb/GMM/1024/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/1024/fold_2/temp/subdirectory/preprocessed/


../../bin/verify.py config_GMM_2048_fold1.py database_GMM_2048_fold1.py
rm -rf results/closedset_cfpb/GMM/2048/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/2048/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_GMM_2048_fold2.py database_GMM_2048_fold2.py
rm -rf results/closedset_cfpb/GMM/2048/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/GMM/2048/fold_2/temp/subdirectory/preprocessed/
