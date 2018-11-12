#Renomeia as extensão dos arquivos 
import os
import re
path =  os.getcwd()
filenames = os.listdir(path)
new_ext = 'wav'
for filename in filenames:
    file_ext = os.path.splitext(filename)[1]
    if old_ext == file_ext:
        newfile = filename.replace(old_ext, new_ext)
        os.rename(filename, newfile)
