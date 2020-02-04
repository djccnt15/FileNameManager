import os, shutil
import pandas as pd

prt1 = 'Set working dir:'
print(prt1) # set working dir
file_dir = str(input())
os.chdir(file_dir)

files = os.listdir() # file list of dir
cfname = list(os.path.abspath(__file__).split('\\')).pop()
if cfname in files: files.remove(cfname) # remove current file from list of dir
else : pass

files = pd.DataFrame(files)
print(files)
files.to_csv('file names.csv', header=0, index=0)