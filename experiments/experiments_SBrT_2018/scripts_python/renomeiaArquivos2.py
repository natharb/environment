#Renomeia arquivos .wav
import os
import re
path =  os.getcwd()
filenames = os.listdir(path)
new_ext = '.wav'
for filename in filenames:
    file_ext = os.path.splitext(filename)[1]
    if file_ext == '.WAV':
        newfile = filename.replace(file_ext, new_ext)
        os.rename(filename, newfile)
