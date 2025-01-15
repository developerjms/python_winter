#211
'''
안녕
Hi
'''

#212
'''
7
15
'''
# 213
# 파라미터값이 없어서

# 214
#문자열과 숫자를 더하지 못 하여서서

#215
def Print_With_Smaile(string):
    print(string, ":D")

#216
Print_With_Smaile('안녕하세요')

#217
def print_upper_price(int):
    print(int*1.3)

#218
def print_sum(a, b):
    print(a+b)

#219
def print_arithmetic_operation(a, b):

    print(a, ' + ', b, ' = ', a+b)
    print(a, ' - ', b, ' = ', a-b)
    print(a, ' * ', b, ' = ', a*b)
    print(a, ' / ', b, ' = ', a/b)

print_arithmetic_operation(3, 4)

# 220
def print_max(a, b, c):
    # if a< b:
    #     if a<c:
    #         print(a)
    # elif b < c:
    #     print(b)
    # else:
    #     print(c)
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)

print_max(20, 15, 10)

