from sklearn.model_selection import StratifiedKFold
from collections import Counter

X = []
y = []
arquivo = open('todos.txt', 'r')
for line in arquivo:
	strg,label = line.split('  ')
	X.append(line)
	y.append(label)

skf = StratifiedKFold(n_splits=10)
skf.get_n_splits(X, y)

index = 1
for train_index, test_index in skf.split(X, y):
    #print("TRAIN:", train_index)
    #print("TEST:", test_index)
    #print("-------------------Aqui eh o Vetor de Treino-----------------------") 
    for i in train_index:
        file = open("train_world" + str(index) +".lst","a")
        file.write(X[i])
    file.close() 
    #print("-------------------Aqui eh o Vetor de Teste------------------------")
    for j in test_index:
        file = open("for_test" + str(index) + ".lst","a")
        file.write(X[j])
    file.close()

    index = index + 1
	