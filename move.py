import os 
import shutil
source= input("Enter source folder name:")
dest= input("Enter dest folder name:")
source=source+'/'
dest=dest+'/'
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.move((source+file),dest)