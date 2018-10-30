#convert stereo to mono
import subprocess
import os
import re
	
path =  os.getcwd()
filenames = os.listdir(path)
for line in filenames:
    line = "ffmpeg -i " + os.path.join(path, line) + " -ac 1 -ar 16000 " + os.path.join(path, "converted"+line)
    subprocess.call(line, shell=True)


