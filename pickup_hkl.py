import numpy as np

# original mrc size
original_mrc_size_x = 131
original_mrc_size_y = 101
original_mrc_size_z = 76

# cutoff mrc size - even
cutoff_mrc_size_x = 130
cutoff_mrc_size_y = 100
cutoff_mrc_size_z = 76

# voxel length
mrc_unit_length = 0.403

center = [
    cutoff_mrc_size_x/2 * mrc_unit_length,
    cutoff_mrc_size_y/2 * mrc_unit_length,
    cutoff_mrc_size_z/2 * mrc_unit_length
]

# read voxel data
voxel_data = []
while True:
    try:
        x, y, z, v = map(float, input().split())
        x -= center[0]
        y -= center[1]
        z -= center[2]
        # print('\t{0:.6f}\t{1:.6f}\t{2:.6f}\t{3:.6f}'.format(x, y, z, v, '.6f'))
        voxel_data.append([x, y, z, v])
    except EOFError:
        break

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

reciprocal_lattice_vector_a = 2 * np.pi * np.cross(unit_cell_tv_y, unit_cell_tv_z) / unit_cell_volume
reciprocal_lattice_vector_b = 2 * np.pi * np.cross(unit_cell_tv_z, unit_cell_tv_x) / unit_cell_volume
reciprocal_lattice_vector_c = 2 * np.pi * np.cross(unit_cell_tv_x, unit_cell_tv_y) / unit_cell_volume

reciprocal_lattice_vector = np.array([
    reciprocal_lattice_vector_a,
    reciprocal_lattice_vector_b,
    reciprocal_lattice_vector_c
])

hkl_range = 1


def main():
    for h in range(-hkl_range, hkl_range):
        for k in range(-hkl_range, hkl_range):
            for l in range(-hkl_range, hkl_range):
                coord = h * reciprocal_lattice_vector_a + \
                        k * reciprocal_lattice_vector_b + \
                        l * reciprocal_lattice_vector_c
                h_value_coord = coord[0] // mrc_unit_length * mrc_unit_length
                k_value_coord = coord[1] // mrc_unit_length * mrc_unit_length
                l_value_coord = coord[2] // mrc_unit_length * mrc_unit_length
                value = search_value(h_value_coord, k_value_coord, l_value_coord)
                print('\t{0}\t{1}\t{2}\t{3:.6f}'.format(h, k, l, value))


def search_value(vx, vy, vz):
    for data in voxel_data:
        if np.isclose(data[0], vx) and np.isclose(data[1], vy) and np.isclose(data[2], vz):
            return data[3]
    print('pick up failed')


if __name__ == '__main__':
    main()
