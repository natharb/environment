#!/bin/sh

../../bin/verify.py config_SVM_256_crossdataset.py database_SVM_256_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/SVM/256/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/SVM/256/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_512_crossdataset.py database_SVM_512_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/SVM/512/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/SVM/512/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_1024_crossdataset.py database_SVM_1024_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/SVM/1024/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/SVM/1024/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_2048_crossdataset.py database_SVM_2048_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/SVM/2048/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/SVM/2048/temp/subdirectory/preprocessed/
