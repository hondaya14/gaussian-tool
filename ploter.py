import sys
import seaborn as sb
import numpy as np
from matplotlib import pyplot as plt
import math

# voxel params
# x_number = 130
# y_number = 100
# z_number = 76
x_number = 170
y_number = 172
z_number = 176



# なに軸の何番目か
section_axis = sys.argv[1]  # x, y, z
# section_number = sys.argv[2]  # 何枚目
print('section axis: ' + section_axis)
# print('section number: ' + section_number)

section_number = 0
if section_axis == 'x':
    section_number = x_number
elif section_axis == 'y':
    section_number = y_number
elif section_axis == 'z':
    section_number = z_number


def validate_axis(xi, yi, zi, sec_num):
    if section_axis == 'x':
        if xi == sec_num:
            return True
    elif section_axis == 'y':
        if yi == sec_num:
            return True
    elif section_axis == 'z':
        if zi == sec_num:
            return True
    return False


# prepare data
data_max = 0
data_min = 100000000
voxel = [[[0] * z_number for i in range(y_number)] for j in range(x_number)]
for k in range(z_number):
    for j in range(y_number):
        for i in range(x_number):
            x, y, z, value = map(float, input().split())
            voxel[i][j][k] = value
            data_max = max(data_max, value)
            data_min = min(data_min, value)

section = np.array([[]])

if section_axis == 'x':
    section = [[0] * z_number for i in range(y_number)]
elif section_axis == 'y':
    section = np.array([[0] * z_number for i in range(x_number)])
elif section_axis == 'z':
    section = np.array([[0] * y_number for i in range(x_number)])


def make_plane(xi, yi, zi):
    if section_axis == 'x':
        section[yi][zi] = voxel[xi][yi][zi]
    elif section_axis == 'y':
        section[xi][zi] = voxel[xi][yi][zi]
    elif section_axis == 'z':
        section[xi][yi] = voxel[xi][yi][zi]


save_path = str(section_axis)+'_section/'
for sn in range(section_number):
    print('section number: ' + str(sn))
    for i in range(x_number):
        for j in range(y_number):
            for k in range(z_number):
                if validate_axis(i, j, k, sn):
                    make_plane(i, j, k)
    plt.figure()
    sb.heatmap(section, cmap='gray', vmax=math.sqrt(data_max), vmin=data_min)
    # plt.show()
    plt.savefig(save_path+section_axis+'_'+str(sn)+'.png')
    plt.clf()
    plt.close()

