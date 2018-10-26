#!/bin/sh

../../bin/verify.py config_iVector_200_crossdataset.py database_iVector_200_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/iVector/200/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/iVector/200/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_150_crossdataset.py database_iVector_150_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/iVector/150/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/iVector/150/temp/subdirectory/preprocessed/

../../bin/verify.py config_iVector_100_crossdataset.py database_iVector_100_crossdataset.py
rm -rf results/crossdataset_cfpb_ynoguti/iVector/100/temp/subdirectory/extracted/ results/crossdataset_cfpb_ynoguti/iVector/100/temp/subdirectory/preprocessed/
