#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
Compute confusion matrix given the four columns file as input

Usage:
  confusion_matrix.py <file>

Options:
  -h --help     Show this screen.

"""
from docopt import docopt


import csv
import numpy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


def _iterate_score_file(filename):
    """Opens the score file for reading and yields the score file line by line in a tuple/list.

    The last element of the line (which is the score) will be transformed to float, the other elements will be str
    """
    opened = open(filename)

    reader = csv.reader(opened, delimiter=' ')
    for splits in reader:
        splits[-1] = float(splits[-1])
        yield splits

args = docopt(__doc__, version='Run experiment')

file = args["<file>"]

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
    scores = numpy.array(scores_dict[key])

    # Argmax using scores
    index = numpy.argmax(scores[:, 2])

    # Getting the expected and the predicted scores
    y_expected.append(int(scores[index, 0]))
    y_predicted.append(int(scores[index, 1]))


#Computing precision, recall, F-measure and support for each class
print('Precision and Recall')
pc = precision_recall_fscore_support(y_expected, y_predicted , average='micro')
print(pc)

print('Accuracy')
ac = accuracy_score(y_expected, y_predicted, normalize=False)
print(ac)

#F1 score reaches its best value at 1 and worst score at 0.
print('F1-Score')
fscore = f1_score(y_expected, y_predicted, average='micro') 
print(fscore)

# Printing the confusion matrix
print('Confusion Matrix')
cm = confusion_matrix(y_expected, y_predicted)
print(cm)
