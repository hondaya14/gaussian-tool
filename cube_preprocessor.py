
# This program is cube file convert to ascii format according to Eos ascii2mrc.
# python3 cub_preprocessor.py < cubefile > new cubefile

# parse header phase
title = str(input())
# print(title)
input()  # 不要行

atom_num = int(input().split()[0])
# print('atomic number ... '+str(atom_num))

dimention = '3'
x_num = int(input().split()[0])
y_num = int(input().split()[0])
z_num = int(input().split()[0])

# cube dimension
print(dimention+' '+str(z_num)+' '+str(y_num)+' '+str(x_num))

# skip phase
for i in range(0, atom_num):
    input()

# data processing phase
line = ''
for i in range(x_num*y_num):
    for j in range(z_num // 6 + 1):
        line += input().replace('\n', ' ')
    print(line)
    line = ''
