import sys


sfname=sys.argv[1]
tfname=sys.argv[2]
# print(sfname, tfname)
sf=open(sfname,'r', encoding='utf-8')
tf=open(tfname,'w', encoding='utf-8')

for i in sf:
    # print(i)
    tf.write(i)

sf.close()
tf.close()