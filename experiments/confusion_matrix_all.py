#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Nathália Alves Rocha Batista (nathbapt@decom.fee.unicamp.br)

"""
Compute confusion matrix given the four columns file as input

Usage:
  confusion_matrix.py <file>

Options:
  -h --help     Show this screen.

"""
import ipdb
import pprint
import sys
import csv
import numpy as np
import fileinput
import os
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

def _iterate_score_file(filename):
  reader = csv.reader(opened, delimiter=' ')
  for splits in reader:
    splits[-1] = float(splits[-1])
    yield splits


def compute(file):
  # Grouping the scores by probe_file
  four_columns = _iterate_score_file(file)
  scores_dict = dict()
  for model_id, probe_id, probe_file, score in four_columns:

    if probe_file not in scores_dict:
      scores_dict[probe_file] = []

    # Grouping using dictionaries
    scores_dict[probe_file].append([int(model_id), int(probe_id), score])

  # Computing the expected/predicted lists
  y_predicted = []
  y_expected = []

  for key in scores_dict:
    # Converting the lists to numpy array to make life easier
    scores = np.array(scores_dict[key])

    # Argmax using scres
    index = np.argmax(scores[:, 2])

    # Getting the expected and the predicted scores
    y_expected.append(int(scores[index, 0]))
    y_predicted.append(int(scores[index, 1]))

  cm = np.array(confusion_matrix(y_expected, y_predicted))
  pc = np.array(precision_recall_fscore_support(y_expected, y_predicted , average='micro'))
  ac = np.array(accuracy_score(y_expected, y_predicted, normalize=False))
  fscore = np.array(f1_score(y_expected, y_predicted, average='micro'))
  return cm, pc, ac, fscore

for file in sys.argv[1:]:
  opened = open(file)
  saida = compute(opened)
  #print(saida)
  total_cm = saida[0]
  total_pc = saida[1]
  total_ac = saida[2]
  total_fscore = saida[3]

for i in range(len(sys.argv[1:])-1):
   total_cm = total_cm + saida[0]
   #total_pc = total_pc + saida[1]
   total_ac = total_ac + saida[2]
   total_fscore = total_fscore + saida[3]

print(total_cm/len(sys.argv[1:]))
#print(total_pc)
print(total_ac/len(sys.argv[1:]))
print(total_fscore/len(sys.argv[1:]))
