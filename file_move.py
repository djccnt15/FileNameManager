'''현재 폴더의 자신을 제외한 모든 파일을 상위 폴더로 이동시켜주는 코드'''
import shutil
from os import listdir

files = listdir() # 해당 디렉터리에 있는 파일들의 리스트
files.remove('file_move.py') # 본 파일을 제외

for f in files: shutil.move(f, '..\\')