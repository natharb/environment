#!/bin/sh

../../bin/verify.py config_GMM_256_crossdataset.py database_GMM_256_crossdataset.py

../../bin/verify.py --preprocessed_directory results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/preprocessed/ --extracted_directory results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/extracted/ config_GMM_512_crossdataset.py database_GMM_512_crossdataset.py

../../bin/verify.py --preprocessed_directory results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/preprocessed/ --extracted_directory results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/extracted/ config_GMM_1024_crossdataset.py database_GMM_1024_crossdataset.py

../../bin/verify.py --preprocessed_directory results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/preprocessed/ --extracted_directory results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/extracted/ config_GMM_2048_crossdataset.py database_GMM_2048_crossdataset.py

rm -rf results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/GMM/256/temp/subdirectory/preprocessed/
rm -rf results/crossdataset_ynoguti_cfpb/GMM/512/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/GMM/512/temp/subdirectory/preprocessed/
rm -rf results/crossdataset_ynoguti_cfpb/GMM/1024/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/GMM/1024/temp/subdirectory/preprocessed/
rm -rf results/crossdataset_ynoguti_cfpb/GMM/2048/temp/subdirectory/extracted/ results/crossdataset_ynoguti_cfpb/GMM/2048/temp/subdirectory/preprocessed/

