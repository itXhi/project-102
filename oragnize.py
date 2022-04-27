from distutils import extension
from importlib.resources import path
import os
import shutil

from_dir = "C:\\Users\\AISHWARYA\\Desktop\\project 102"
to_dir = "C:\\Users\\AISHWARYA\\Desktop\\project 102\\image_file"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    
    if extension == " ":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '\\' +file_name
        path2 = to_dir + '\\'+ "image_file"
        path3 = to_dir + '\\'+ "image_file" + '\\' + file_name
        #print("path1", path1)
        #print("path3", path3)
        
    if extension in ['.docx' , '.pptx', '.xlsx']:
        path1 = from_dir + '\\' +file_name
        path2 = to_dir + '\\'+ "image_file"
        path3 = to_dir + '\\'+ "image_file" + '\\' + file_name


        if os.path.exists(path2): 
           print("Moving " + file_name + ".....") 
           # Move from path1 ---> path3 
           shutil.move(path1, path3) 
        else:
             os.makedirs(path2) 
             print("Moving " + file_name + ".....") 
             shutil.move(path1, path3)
             