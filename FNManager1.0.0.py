import shutil, os
from os import listdir, rename

prompt ='''
1 상위 폴더로 파일 이동
2 파일 이름 앞에 현재 폴더명 추가
3 파일명에서 마지막 - 뒤의 문자열로 파일명 변경

모든 기능은 현재 폴더의 본 파일을 제외한 모든 파일 및 폴더에 적용
기능 선택:'''

print(prompt)

files = listdir() # 해당 디렉터리에 있는 파일들의 리스트
files.remove('filemanager.py') # 본 파일을 제외

input_num = int(input()) # 기능 선택

if input_num == 1: # 상위 폴더로 파일 이동
    for f in files: shutil.move(f, '..\\')

if input_num == 2: # 파일 이름 앞에 현재 폴더명 추가
    folder_name = list(os.getcwd().split('\\')).pop() # 경로에서 현재 폴더명 추출
    for name in files:
        newname = name.replace(name, folder_name + '-' + name)
        rename(name, newname)

if input_num == 3: # 파일명에서 마지막 - 뒤의 문자열로 파일명 변경
    for name in files:
        newname = name.replace(name, name.split('-')[-1])
        rename(name, newname)
