#This script helps you to backup the contents of a directory
#files and directories fast . Simply write the source path and 
#the path of the folder you wish to save your files to.

import os, sys
import shutil
import errno

src = input("Give the path of  the folder you wish to backup:")
dest = input("Give the path of the destination folder:")

print("==========================================")
src_files = os.listdir(src)

errors_n= 0
dir_n = 0
file_n = 0
 
def copy(src, dest):
    global dir_n,file_n,errors_n
    try:
        shutil.copytree(src, dest)
        print("[*]Copying Directory: "+dest)
        dir_n+=1
    except OSError as e:
        #source is a file
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
            file_n+=1
        else:
            print('[-]Error: %s' % e)
            errors_n+=1



for file_name in src_files:
    temp = ""
    full_file_name = os.path.join(src, file_name)

    #print(file_name)
    if (os.path.isfile(full_file_name) == 0):
        temp = dest + '/'+ file_name
    else:
        print("[*]Copying File: " + file_name)
        temp = dest
    #print(temp)
    copy(full_file_name , temp)


total_files_src = len(os.listdir(src))
total_copied = file_n + dir_n

print("==========================================")
print("[+] Done - Succesfuly copied ",total_copied,"out of",total_files_src,"-(Total Errors: " ,errors_n," ,Files Copied: ",file_n," ,Folders Copied: ",dir_n,")")
