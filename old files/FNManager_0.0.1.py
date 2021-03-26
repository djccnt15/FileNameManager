import os, shutil

prt1 = 'Set working dir:'
prt2 ='''
1 Set working dir
2 Get current working dir
3 Check the file/folder list
4 Add current folder name in front of file/folder names
5 Add user input in front of file/folder names
6 Cut file names until delimiter
7 Move all to upper dir
8 Exit

Every functions work for every files/folders in working dir
Select a function:'''
prt3 = "input your delimiter(s), '.'is unavailable:"
prt4 = 'input your own word(s):'

print(prt1) # set working dir
file_dir = str(input())
os.chdir(file_dir)

print(prt2) # select a function
input_num = input()
while True:
    files = os.listdir() # file list of dir
    cfname = list(os.path.abspath(__file__).split('\\')).pop()
    if cfname in files: files.remove(cfname) # remove current file from list of dir
    else : pass

    if input_num == '1': # set working dir
        print(prt1)
        file_dir = str(input())
        os.chdir(file_dir)

    elif input_num == '2': print(os.getcwd()) # get current working dir

    elif input_num == '3': print(files) # check the file/folder list

    elif input_num == '4': # add current folder name in front of file/folder names
        print(prt3)
        delimiter = str(input())
        if delimiter == '.':
            print("'.' is unavailable")
            pass
        else:
            folder_name = list(os.getcwd().split('\\')).pop() # get current folder name
            for f in files:
                newname = f.replace(f, folder_name + '%s' %delimiter + f )
                os.rename(f, newname)

    elif input_num == '5': # add user input in front of file/folder names
        print(prt4)
        user_input = str(input())
        print(prt3)
        delimiter = str(input())
        if delimiter == '.':
            print("'.'is unavailable")
            pass
        else:
            for f in files:
                newname = f.replace(f, user_input + '%s' %delimiter + f )
                os.rename(f, newname)

    elif input_num == '6': # cut file names until delimiter
        print(prt3)
        delimiter = str(input())
        if delimiter == '.':
            print("'.'is unavailable")
            pass
        else:
            for f in files:
                newname = f.replace(f, f.split('%s' %delimiter)[-1])
                os.rename(f, newname)

    elif input_num == '7': # move all to upper dir
        for f in files: shutil.move(f, '..\\')

    elif input_num == '8': break

    print(prt2) # select a function
    input_num = input()
