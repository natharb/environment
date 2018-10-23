#!/bin/sh

../../bin/verify.py config_iVector_200_fold1.py database_iVector_200_fold1.py
rm -rf results/closedset_cfpb/iVector/200/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/200/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_iVector_200_fold2.py database_iVector_200_fold2.py
rm -rf results/closedset_cfpb/iVector/200/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/200/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_300_fold1.py database_iVector_300_fold1.py
rm -rf results/closedset_cfpb/iVector/300/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/300/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_iVector_300_fold2.py database_iVector_300_fold2.py
rm -rf results/closedset_cfpb/iVector/300/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/300/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_400_fold1.py database_iVector_400_fold1.py
rm -rf results/closedset_cfpb/iVector/400/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/400/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_iVector_400_fold2.py database_iVector_400_fold2.py
rm -rf results/closedset_cfpb/iVector/400/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/400/fold_2/temp/subdirectory/preprocessed/
