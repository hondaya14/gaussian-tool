# This program is cube file convert to ascii format according to Eos ascii2mrc.
# python3 cub_preprocessor.py < cubefile > new cubefile

# parse header phase
title = str(input())
# print(title)
input()  # 不要行

atom_num = int(input().split()[0])
# print('atomic number ... '+str(atom_num))

dimension = '3'
x_num = int(input().split()[0])
y_num = int(input().split()[0])
z_num = int(input().split()[0])

# cube dimension
print(dimension+' '+str(x_num)+' '+str(y_num)+' '+str(z_num))

# skip phase
for i in range(0, atom_num):
    input()

cube = [[[[''] for z in range(z_num)] for y in range(y_num)] for x in range(x_num)]

for i in range(x_num):
    for j in range(y_num):
        lines = ''
        for line in range(z_num // 6 + 1):
            lines += input().replace('\n', ' ')
        z_column = lines.split()
        for k in range(z_num):
            cube[i][j][k] = z_column[k]


for i in range(z_num):
    for j in range(y_num):
        line = ''
        for k in range(x_num):
            # print(cube[k][j][i], end=' ')
            line += ' ' + cube[k][j][i]
        print(line)
