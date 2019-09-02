'''파일명에서 마지막 - 뒤의 문자열로 파일명 변경해주는 코드'''
from os import listdir, rename

files = listdir()
print(files)
files.remove('file_rename_undo.py') # 본 파일을 제외
for name in files:
    newname = name.replace(name, name.split('-')[-1])
    print(newname)
    rename(name, newname)