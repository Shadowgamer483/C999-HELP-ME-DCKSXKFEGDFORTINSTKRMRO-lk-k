import os
import shutil
src=input("enter source folder name :)  ")
destination=input("enter destination name")
src=src+"/"
destination=destination+"/"
listoffiles=os.listdir(src)
for file in listoffiles:
    shutil.copy((src+file),destination)





