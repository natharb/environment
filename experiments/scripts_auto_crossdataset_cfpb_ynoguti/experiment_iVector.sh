#!/bin/sh

../../bin/verify.py config_iVector_200_crossdataset.py database_iVector_200_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/iVector/200/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/iVector/200/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_300_crossdataset.py database_iVector_300_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/iVector/300/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/iVector/300/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_400_crossdataset.py database_iVector_400_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/iVector/400/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/iVector/400/temp/subdirectory/preprocessed/