import os
import shutil

# write the name of the directory here,
# that needs to get sorted
# path = '/Users/annikamishra'

path = input("enter the name of the directory to be sorted- ")


# this will create a properly organised 
# list with all filename that is 
# there in the directory
list_of_files = os.listdir(path)

# this will go through each and every file
for file in list_of_files: 
    name, ext = os.path.splitext(file)

    # this is going to store the extension type
    ext = ext[1:]

    # this forces the next iteration,
    # if it is a directory

    if ext == '':
        continue
    
    # this will move the file to the directory
    # where the name 'ext' already exists
if os.path.exists(path+'/'+ext): 
    shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

# this will create a new directory, 
# if the directory does not already exist 

else: 
    os.makedirs(path+'/'+ext) 
    shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
