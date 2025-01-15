f1=open('a.txt','r', encoding='utf-8')
f2=open('b.txt','w', encoding='utf-8')

for line in f1:
    dat=line.split(',')
    data=[]
    data.append(dat[0].strip())
    for i in range(1,len(dat)):
        data.append(int(dat[i].strip()))
    data.append(data[1]+data[2]+data[3])
    print(data)
    res=",".join(str(i) for i in data)
    f2.writelines(res+"\n")

f1.close()
f2.close()