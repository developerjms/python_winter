f=open('c.txt', 'w')
for i in range(10):
    # f. write(str(i)+"\n") #변수출력, 한줄 작성시 사용
    f. writelines(str(i)+'\n') #리스트(군집체) 출력, 여러줄 작성시 사용
f.close()

