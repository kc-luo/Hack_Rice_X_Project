import os
path = 'E:\\_Kevin\\Code\\Hack_Rice_X_Project\\trainingDataPreprocessing\\img_y'
new_path2 = 'E:\\_Kevin\\Code\\Hack_Rice_X_Project\\trainingDataPreprocessing\\validation_2'
new_path = 'E:\\_Kevin\\Code\\Hack_Rice_X_Project\\trainingDataPreprocessing\\validation_y'

#获取该目录下所有文件，存入列表中
fileList = os.listdir(new_path2)

n=0
for i in fileList:
    #设置旧文件名（就是路径+文件名）
    oldname = new_path2 + os.sep + fileList[n]   # os.sep添加系统分隔符
    
    #设置新文件名
    newname = new_path + os.sep + "{:04}".format(n+3601)+'.png'
    
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)
    
    n += 1