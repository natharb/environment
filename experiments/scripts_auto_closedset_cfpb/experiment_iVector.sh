#!/bin/sh

#../../bin/verify.py config_iVector_200_fold1.py database_iVector_200_fold1.py
#rm -rf results/closedset_cfpb/iVector/200/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/200/fold_1/temp/subdirectory/preprocessed/
#../../bin/verify.py config_iVector_200_fold2.py database_iVector_200_fold2.py
#rm -rf results/closedset_cfpb/iVector/200/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/200/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_150_fold1.py database_iVector_150_fold1.py
rm -rf results/closedset_cfpb/iVector/150/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/150/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_iVector_150_fold2.py database_iVector_300_fold2.py
rm -rf results/closedset_cfpb/iVector/150/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/150/fold_2/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_100_fold1.py database_iVector_100_fold1.py
rm -rf results/closedset_cfpb/iVector/100/fold_1/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/100/fold_1/temp/subdirectory/preprocessed/
../../bin/verify.py config_iVector_100_fold2.py database_iVector_400_fold2.py
rm -rf results/closedset_cfpb/iVector/100/fold_2/temp/subdirectory/extracted/ results/closedset_cfpb/iVector/100/fold_2/temp/subdirectory/preprocessed/
