prim_num_count = 0
prim_nume = []
for i in range(2, 101):
    sw = 0
    for j in range(2, i):
        prim_num_count += 1
        if i % j == 0:
            sw= 1
    if sw == 0:
        prim_nume.append(i)

print("소수 : ", prim_nume)
print(len(prim_nume))
print("소수 회전수 : ", prim_num_count)

prim_num_count = 0
prim_nume=[]

for i in range(2,101):
    sw = 0
    for j in range(2, i):
        prim_num_count += 1
        if i % j == 0:
            sw=1
            break
    if sw==0:
        prim_nume.append(i)

print("소수 : ", prim_nume)
print(len(prim_nume))
print("소수 회전수 : ", prim_num_count)
