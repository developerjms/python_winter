n=int(input('마방진 사이즈 입력:'))
print('\n내가 만든 마방진 출력')
square = [[0] * n for _ in range(n)]
row = 0
col = n // 2
for k in range(1, n * n + 1):  # 1부터 25까지
    square[row][col] = k
    row -= 1
    col -= 1
    if row < 0:
        row += n
    if col < 0:
        col += n
    if square[row][col] > 0:
        row = (row + 2) % n
        col = (col + 1) % n

for row in square:
    for col in row:
        print("%2d "%col, end='')
    print()