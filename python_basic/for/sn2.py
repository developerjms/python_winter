n=int(input('사이즈:'))
arr=[[0 for j in range(n)]for i in range(n)]
k=0
sw=1
i=0
j=-1
while True:
    for p in range(n):
        k+=1
        j+=sw
        arr[i][j]=k
    n-=1
    if n > 0:
        for p in range(n):
            k+=1
            i+=sw
            arr[i][j] = k
        sw*=-1
    else:
        break

for i in arr:
    for j in i:
        print('%2d '%j,end='')
    print()





    