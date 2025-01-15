import random

n=int(input('사이즈:'))
arr=[[0 for j in range(n)]for i in range(n)]


# 조건부 = 오른쪽 상향을 했을때 

m = n-1
i = random.randint(0, m)
j = random.randint(0, m)
num = 1
arr[i][j] = num
no=0
for i in range(0, (n**2)+1, 1):
    no += i
print(no)

while num != no:
    if i > 0:
        i += n
    elif j >= n:
        j = 0
        i -=1
        continue
    elif arr[i-1][j+1] == 0:
        i -=1
        j +=1
        num +=1
        arr[i][j] = num
    elif arr[i][j] > 0:
        num+=1
        i+=2
        j-=1
        arr[i][j] = num
        
    

print(i, j, m, n, num)
print(arr)

    # if j > n:
    #     i = 0
    #     arr[i][j] = num
    # elif j < 0:
    #     i = m
    #     arr[i][j] = num
    # elif i < 0:
    #     j = 0
    #     arr[i][j] = num
    # elif i > n:
    #     j = m
    #     arr[i][j] = num
        
    # elif arr[i][j] != 0:
    #     arr[i][j+1] = num
        

    # else:
    #     arr[i][j] = num
     

        




