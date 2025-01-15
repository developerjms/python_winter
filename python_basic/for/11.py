# for j in range(2,10):
#     print(j, '단', end="\t\t")
# print("")
# for i in range(1, 10, 1):
#     print("")
#     for x in range(2, 10, 1):
#         print(i, " * ", x, " = " , i*x, end="\t")

# list = [1,10,30,20,90]
# for i in list:
#     print(i)

# for i in range(len(list)):
#     print('%d번째 데이터 = %d'%(i+1,list[i]))

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 ", treeHit, '번 찍었습니다.')
#     if treeHit == 10:
#         print("나무를 넘어갑니다.")
#         break

# for i in range(0, 10, 1):
#     print("나무를 ", i+1, '번 찍었습니다.')

# menu='''
# ==MENU==
# 1. 짜장면
# 2. 짬뽕
# 3. 우동
# 4. 볶음밥
# 5. 탕수육
# '''

# while True:
#     print(menu)
#     sel = int(input('메뉴선택 : '))
#     if sel == 1:
#         menu = '짜장면'
#         print("짜장면을 선택하셨습니다.")
#     elif sel == 2:
#         menu = '짬뽕'
#         print("짬뽕을 선택하셨습니다.")
#     elif sel == 3:
#         menu = '우동'
#         print("우동을 선택하셨습니다.")
#     elif sel == 4:
#         menu = '볶음밥'
#         print("볶음밥을 선택하셨습니다.")
#     elif sel == 5:
#         menu = '탕수육'
#         print("탕수육을 선택하셨습니다.")
#     else :
#         print("메뉴를 다시 선택해주세요")
#         continue
#     print(menu, '나왔습니다.')
#     break


# 달팽이 행렬
# 5칸 5칸 내로 숫자 돌리기
# a = [1, 2, 3]

# n = int(input('사이즈 : '))
# arr = [[ 0 for j in range(n)] for i in range(n)]

arr = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
arr[0][1] = 1
    
print(arr)





# 내가만든 마방진 출력
# 대각 우상향으로 이동하며 칸이없으면 반대로로 이동
# 이동공간에 데이터가 있으면 밑으로 한칸 이동
# 대각선 


#스도쿠 게임 만들기

 