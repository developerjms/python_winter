#231
'''
전역변수를 외부에서 사용하므로 오류가 발생한다
'''

#232
# def make_url(str):
#     print('www.'+ str +'.com')

# make_url('naver')

#233
# def make_list(str):
#     list=[]
#     for i in str:
#         list.append(i)
#     print(list)
# make_list('abcd')

#234
# def pickup_even(a):
#     list=[]
#     for i in a:
#         if int(i) % 2 == 0:
#             list.append(i)
#     print(list)
# pickup_even(([3,4,5,6,7,8]))

#235
def convert_int(string):
    print(int(string.replace(',', '')))
convert_int("1,234,567")

#236





