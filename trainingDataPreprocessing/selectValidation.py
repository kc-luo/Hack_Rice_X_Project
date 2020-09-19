import os
import random

path = 'E:\\_Kevin\\Code\\Hack_Rice_X_Project\\trainingDataPreprocessing\\img_y'
new_path = 'E:\\_Kevin\\Code\\Hack_Rice_X_Project\\trainingDataPreprocessing\\validation_y'

#获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
random.shuffle(fileList)
for i in range(400):
    file_name = fileList[i]
    file_id = file_name.split("/")[-1]
    file_id = file_id[:len(file_id) - 4]
    oldname = path + os.sep + file_id + '.png'
    newname = new_path + os.sep + file_id + '.png'
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)