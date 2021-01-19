import numpy as np
import sys

voxel_file = sys.argv[1]
hkl_ref_file = sys.argv[2]

# original mrc size
# original_mrc_size_x = 131
# original_mrc_size_y = 101
# original_mrc_size_z = 76
original_mrc_size_x = 170
original_mrc_size_y = 172
original_mrc_size_z = 176

# cutoff mrc size - even
cutoff_mrc_size_x = 170
cutoff_mrc_size_y = 172
cutoff_mrc_size_z = 176

# voxel length
# mrc_unit_length = 0.403
mrc_unit_length = 0.336

center = [
    cutoff_mrc_size_x / 2,
    cutoff_mrc_size_y / 2,
    cutoff_mrc_size_z / 2
]


# read voxel data
voxel_data = []
with open(voxel_file) as vf:
    vl = vf.readlines()
    cx = 0
    for line in vl:
        try:
            x, y, z, v = map(float, line.split())
            # x, y, z を ボクセルの整数座標に変換
            x = round(x / mrc_unit_length)
            y = round(y / mrc_unit_length)
            z = round(z / mrc_unit_length)

            # 逆空間(Å^-1)に変換
            x = (x - cutoff_mrc_size_x / 2) / (cutoff_mrc_size_x * mrc_unit_length)
            y = (y - cutoff_mrc_size_y / 2) / (cutoff_mrc_size_y * mrc_unit_length)
            z = (z - cutoff_mrc_size_z / 2) / (cutoff_mrc_size_z * mrc_unit_length)
            # print('\t{0}\t{1}\t{2}\t{3}'.format(x, y, z, v))
            voxel_data.append([x, y, z, v])

        except EOFError:
            break


# フーリエボクセル1個の幅
voxel_unit_length_x = 1 / (cutoff_mrc_size_x * mrc_unit_length)
voxel_unit_length_y = 1 / (cutoff_mrc_size_y * mrc_unit_length)
voxel_unit_length_z = 1 / (cutoff_mrc_size_z * mrc_unit_length)

# unit cell parameters
unit_cell_tv_x = [7.1178, 0, 0]
unit_cell_tv_y = [0, 9.6265, 0]
unit_cell_tv_z = [-1.39567, 0, 11.81314]

unit_cell_tv = np.array([
    unit_cell_tv_x,
    unit_cell_tv_y,
    unit_cell_tv_z
])

# unit cell volume
unit_cell_volume = np.dot(np.cross(unit_cell_tv_x, unit_cell_tv_y), unit_cell_tv_z)

reciprocal_lattice_vector_a = np.cross(unit_cell_tv_y, unit_cell_tv_z) / unit_cell_volume
reciprocal_lattice_vector_b = np.cross(unit_cell_tv_z, unit_cell_tv_x) / unit_cell_volume
reciprocal_lattice_vector_c = np.cross(unit_cell_tv_x, unit_cell_tv_y) / unit_cell_volume

reciprocal_lattice_vector = np.array([
    reciprocal_lattice_vector_a,
    reciprocal_lattice_vector_b,
    reciprocal_lattice_vector_c
])

# hkl reference
hkl = []
with open(hkl_ref_file) as hrf:
    hl = hrf.readlines()
    for lines in hl:
        h, k, l, *values = lines.split()
        hkl.append([int(h), int(k), int(l)])


def main():
    # hkl.insert(0, [0, 0, 0])
    for e in hkl:
        h, k, l = e[0], e[1], e[2]

        # referenceで読み込んだh,k,lに対応するフーリエ空間の座標
        fourier_coord = h * reciprocal_lattice_vector_a + \
                        k * reciprocal_lattice_vector_b + \
                        l * reciprocal_lattice_vector_c

        # 特定のhklの点が対応するボクセルの座標
        target_voxel_x = round(fourier_coord[0] / voxel_unit_length_x) * voxel_unit_length_x
        target_voxel_y = round(fourier_coord[1] / voxel_unit_length_y) * voxel_unit_length_y
        target_voxel_z = round(fourier_coord[2] / voxel_unit_length_z) * voxel_unit_length_z

        value = search_value(target_voxel_x, target_voxel_y, target_voxel_z)
        print('\t{0}\t{1}\t{2}\t{3:.6f}'.format(h, k, l, value), flush=True)


def search_value(vx, vy, vz):
    for data in voxel_data:
        if np.isclose(data[0], vx) and np.isclose(data[1], vy) and np.isclose(data[2], vz):
            return data[3]
    print('pick up failed')
    exit(1)


if __name__ == '__main__':
    main()
