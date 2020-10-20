#  _ _ _ _____ _ _ _ _____ _____ _____
# | | | |  _  | | | |     |   __|__   |
# | | | |     | | | |  |  |__   |   __|
# |_____|__|__|_____|_____|_____|_____|
#
# (C) 2019 by Wawrzyniec L. Dobrucki
# wawosz@gmail.com
#
# Syntax: python3 inveon2slicer.py <file.img.hdr>
#
# Parsing script to read data from *.img.hdr header to slicer3D *.nrrh header
# and rename *.img binary file to *.raw file read by slicer3D
#
# Example slicer3D header file (*.nrrh):
#


import sys
import os


def main():
    # find base and extension of the inveon file
    inveon_file = sys.argv[1]
    base, extension = os.path.splitext(inveon_file)
    # print('base: ', base)
    # print('extension: ', extension)

    # read the *.img.hdr file
    file = open(inveon_file, "r")
    lines = file.readlines()
    file.close()

    # first line of *.nhdr file
    nhdr = [None] * 8  # initialize list
    nhdr[0] = 'NRRD0001' + '\n'

    # enter name of new file
    filename = input('Enter new filename: ')

    # look for patterns such as filename, resolution, pixel dimension
    for line in lines:
        # find data type
        if line.find('data_type') != -1:
            data_type = line.split()
            print(data_type)
            if data_type[1] == '2':
                nhdr[1] = 'type: int16' + '\n'  # 2-byte integer - Intel style
            else:
                nhdr[1] = 'type: float' + '\n'  # 4-byte float - Intel style

        if line.find('x_dimension') != -1:
            x_dim = line.split()
            print(x_dim)
        if line.find('y_dimension') != -1:
            y_dim = line.split()
            print(y_dim)
        if line.find('z_dimension') != -1:
            z_dim = line.split()
            print(z_dim)
        if line.find('pixel_size_x') != -1:
            x_spacing = line.split()
            print(x_spacing)
        if line.find('pixel_size_y') != -1:
            y_spacing = line.split()
            print(y_spacing)
        if line.find('pixel_size_z') != -1:
            z_spacing = line.split()
            print(z_spacing)

    nhdr[2] = 'dimension: 3' + '\n'
    nhdr[3] = 'sizes: ' + x_dim[1] + ' ' + y_dim[1] + ' ' + z_dim[1] + '\n'
    nhdr[4] = 'spacings: ' + x_spacing[1] + ' ' + y_spacing[1] + ' ' + z_spacing[1] + '\n'
    nhdr[5] = 'encoding: raw' + '\n'
    nhdr[6] = 'data file: ' + base + '\n'
    nhdr[7] = 'endian: little' + '\n'

    # save list as lines to the new file
    file = open(filename + '.nhdr', "w+")
    file.writelines(nhdr)
    file.close()


main()
