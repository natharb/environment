#!/bin/sh

../../bin/verify.py config_SVM_32_crossdataset.py database_SVM_32_crossdataset.py
rm -rf results/crossdataset_ynoguti_cfpb/SVM/32/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/SVM/32/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_64_crossdataset.py database_SVM_64_crossdataset.py
rm -rf results/crossdataset_ynoguti_cfpb/SVM/64/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/SVM/64/temp/subdirectory/preprocessed/

../../bin/verify.py config_SVM_128_crossdataset.py database_SVM_128_crossdataset.py
rm -rf results/crossdataset_ynoguti_cfpb/SVM/128/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/SVM/128/temp/subdirectory/preprocessed/
