from sklearn.model_selection import StratifiedKFold

X = []
y = []
arquivo = open('for_test10.lst', 'r')
for line in arquivo:
	strg,label = line.split('  ')
	X.append(line)
	y.append(label)

skf = StratifiedKFold(n_splits=2)
skf.get_n_splits(X, y)

index = 1
for train_index, test_index in skf.split(X, y):
    #print("-------------------Vetor de Modelos (MAP)-----------------------") 
    for i in train_index:
        file = open("for_models" + str(index) +".lst","a")
        file.write(X[i])
    file.close() 
    #print("-------------------Vetor de Probes------------------------")
    for j in test_index:
        file = open("for_probes" + str(index) + ".lst","a")
        file.write(X[j])
    file.close()

    index = index + 1



