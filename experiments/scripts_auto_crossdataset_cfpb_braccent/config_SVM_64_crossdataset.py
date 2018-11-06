#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#Nathália Alves Rocha Batista (nathbapt@decom.fee.unicamp.br)

import sys
sys.path.insert(0, '.')

import bob.bio.spear
import bob.bio.gmm
import numpy
import scipy.spatial

temp_directory = './results/crossdataset_cfpb_braccent/SVM/64/temp/'
result_directory = './results/crossdataset_cfpb_braccent/SVM/64/results/'
sub_directory = 'subdirectory'

database = 'database_SVM_64_crossdataset.py'

groups = ['dev']
#groups = ['dev', 'eval']

preprocessor = bob.bio.spear.preprocessor.Energy_2Gauss(max_iterations = 10, convergence_threshold = 0.0005, variance_threshold = 0.0005,  win_length_ms = 20., win_shift_ms = 10., smoothing_window = 10)

extractor = bob.bio.spear.extractor.Cepstral(win_length_ms = 25, win_shift_ms = 10, n_filters = 24 , dct_norm = False, f_min = 0, f_max = 4000, delta_win = 2, mel_scale = True, with_energy = True, with_delta = True, with_delta_delta = True, n_ceps = 19, pre_emphasis_coef = 0.97)

algorithm = bob.bio.gmm.algorithm.SVMGMM(number_of_gaussians = 64, kmeans_training_iterations = 10, gmm_training_iterations = 10,
training_threshold = 5e-4, variance_threshold = 5e-4, update_weights = True, update_means = True, update_variances = True, relevance_factor = 4, gmm_enroll_iterations = 1, responsibility_threshold = 0, INIT_SEED = 5489)

#parallel = 40
#verbose = 2
