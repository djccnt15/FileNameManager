'''파일 이름 앞에 현재 폴더명을 붙여주는 코드'''
import os
from os import listdir, rename

folder_name = list(os.getcwd().split('\\')).pop() # 경로에서 현재 폴더명 추출
files = listdir() # 해당 디렉터리에 있는 파일들의 리스트
files.remove('file_rename.py') # 본 파일을 제외

for name in files:
    newname = name.replace(name, folder_name + '-' + name)
    rename(name, newname)