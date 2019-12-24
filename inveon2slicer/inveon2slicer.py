#!/usr/bin/env python3

#
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


def main():
    # read the *.img.hdr file
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    file.close()

    # look for patterns such as filename, resolution, pixel dimension
    for line in lines:
        print(line)  # display line


main()
