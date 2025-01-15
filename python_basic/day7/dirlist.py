# import glob

# dirlist = glob.glob("C:\\Users\\USER\\Desktop\\python\\python\\day7\\*.*")
# print(dirlist)

# import pickle
# f = open("test")


import zipfile

#파일 합치기
with zipfile.ZiqFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# with zipfile.ZipFile('mytext.zip') as myzip:
    