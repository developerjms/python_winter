f = open('a.txt', 'r', encoding='utf-8')

lines = f.readlines()
print('readlines로 출력 : ', lines)

f.close()

f = open('a.txt', 'r', encoding='utf-8')

# ==========================================

while True:
    line = f.readline()
    if not line:
        break
    print('readline으로 출력 : ',line)

f.close()

# ==========================================

f = open('a.txt', 'r', encoding='utf-8')

s=f.read() # 전체가 문자열로 읽기
print('read로 출력 : ', s)

for i in s:
    print(i)

for line in f:
    print('read 반복문 출력력 : ',line)

f.close()