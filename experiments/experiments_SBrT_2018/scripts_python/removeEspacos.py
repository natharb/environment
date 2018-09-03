#Remove todos os espacos
import os
import re
path =  os.getcwd()
filenames = os.listdir(path)
print(filenames)
for filename in filenames:
    saida = filename.replace(" ", "")
    os.rename(filename, saida)
