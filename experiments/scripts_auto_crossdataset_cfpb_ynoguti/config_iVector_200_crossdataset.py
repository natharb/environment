#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#Nathália Alves Rocha Batista (nathbapt@decom.fee.unicamp.br)

import sys
sys.path.insert(0, '.')

import bob.bio.spear
import bob.bio.gmm
import numpy
import scipy.spatial

temp_directory = './results/crossdataset_cfpb_ynoguti/iVector/200/temp/'
result_directory = './results/crossdataset_cfpb_ynoguti/iVector/200/results/'
sub_directory = 'subdirectory'

database = 'database_iVector_200_crossdataset.py'

groups = ['dev']
#groups = ['dev', 'eval']

preprocessor = bob.bio.spear.preprocessor.Energy_2Gauss(max_iterations = 10, convergence_threshold = 0.0005, variance_threshold = 0.0005,  win_length_ms = 20., win_shift_ms = 10., smoothing_window = 10)

extractor = bob.bio.spear.extractor.Cepstral(win_length_ms = 25, win_shift_ms = 10, n_filters = 24 , dct_norm = False, f_min = 0, f_max = 4000, delta_win = 2, mel_scale = True, with_energy = True, with_delta = True, with_delta_delta = True, n_ceps = 19, pre_emphasis_coef = 0.97)

algorithm = bob.bio.gmm.algorithm.IVector(subspace_dimension_of_t = 200, tv_training_iterations = 10, update_sigma = True, use_whitening = True, use_lda = False, use_wccn = False, use_plda = False, lda_dim = 50, plda_dim_F  = 50, plda_dim_G = 50, plda_training_iterations = 50, number_of_gaussians = 2048)

parallel = 8
verbose = 2
