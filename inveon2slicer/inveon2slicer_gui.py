#  _ _ _ _____ _ _ _ _____ _____ _____
# | | | |  _  | | | |     |   __|__   |
# | | | |     | | | |  |  |__   |   __|
# |_____|__|__|_____|_____|_____|_____|
#
# (C) 2021 by Wawrzyniec L. Dobrucki
# wawosz@gmail.com
#
# Syntax: python3 inveon2slicer_gui.py
#
# Parsing script to read data from *.img.hdr header to slicer3D *.nrrh header
# and rename *.img binary file to *.raw file read by slicer3D
# GUI version written with PyQt5
#

import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    # Main method: initialize widget (window)
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        # Window properties and geometry
        self.title = 'Inveon to Slicer 3D Converter'
        self.setWindowTitle(self.title)
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 250
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Define widgets
        self.load_label = qtw.QLabel('Load *.hdr file to convert')
        self.load_button = qtw.QPushButton('LOAD')

        self.convert_label = qtw.QLabel('Save converted file as')
        self.convert_button = qtw.QPushButton('CONVERT and SAVE')
        self.convert_button.setEnabled(False)

        self.info_text = qtw.QTextEdit()

        # Define layout and place widgets on the layout
        layout = qtw.QGridLayout()
        layout.addWidget(self.load_label, 0, 0)
        layout.addWidget(self.load_button, 0, 1)
        layout.addWidget(self.convert_label, 1, 0)
        layout.addWidget(self.convert_button, 1, 1)
        layout.addWidget(self.info_text, 3, 1)

        self.setLayout(layout)

        # Define signals and stacks
        self.load_button.clicked.connect(self.getfile)
        self.convert_button.clicked.connect(self.convert_file)

        # Show window and widgets
        self.show()

    # Method: open dialog to select file to load
    def getfile(self):
        self.fname, _ = qtw.QFileDialog.getOpenFileName(self,'Open Inveon header (*.hdr) file to convert', 'c:\\',"Header file (*.hdr)")
        if self.fname:
            self.convert_button.setEnabled(True)
            return self.fname

    # Method: print info and convert file
    def convert_file(self):
        # read the *.img.hdr file
        inveon_file = open(self.fname, "r")
        # get filename only with no path
        base = os.path.basename(self.fname)
        # separate base from extension of a filename
        base, extension = os.path.splitext(base)
        # read lines from inveon *.hdr file for text analysis
        lines = inveon_file.readlines()
        # close the inveon *.hdr file
        inveon_file.close()
        
        # information text to be displayed in a text window
        info = 'File: ' + self.fname + '\n'

        # first line of *.nhdr file
        nhdr = [None] * 8  # initialize list
        nhdr[0] = 'NRRD0001' + '\n'

        # Text analysis: look for patterns such as filename, resolution, pixel dimension
        for line in lines:
            # find data type
            if line.find('data_type') != -1:
                data_type = line.split()
                if data_type[1] == '2':
                    nhdr[1] = 'type: int16' + '\n'  # 2-byte integer - Intel style
                    info = info + 'Data type: \t2-byte integer (Intel style)\n'
                else:
                    nhdr[1] = 'type: float' + '\n'  # 4-byte float - Intel style
                    info = info + 'Data type: \t4-byte float (Intel style)\n'

            if line.find('x_dimension') != -1:
                x_dim = line.split()
                info = info + 'X dimension:\t' + x_dim[1] + ' px \n'
            if line.find('y_dimension') != -1:
                y_dim = line.split()
                info = info + 'Y dimension:\t' + y_dim[1] + ' px \n'
            if line.find('z_dimension') != -1:
                z_dim = line.split()
                info = info + 'Z dimension:\t' + z_dim[1] + ' px \n'
            if line.find('pixel_size_x') != -1:
                x_spacing = line.split()
                info = info + 'X pixel size:\t' + x_spacing[1] + ' mm \n'
            if line.find('pixel_size_y') != -1:
                y_spacing = line.split()
                info = info + 'Y pixel size:\t' + y_spacing[1] + ' mm \n'
            if line.find('pixel_size_z') != -1:
                z_spacing = line.split()
                info = info + 'Z pixel size:\t' + z_spacing[1] + ' mm \n'

        # print information text in info widget
        self.info_text.setPlainText(info)

        # fill nhdr list with info to create *.nhdr file
        nhdr[2] = 'dimension: 3' + '\n'
        nhdr[3] = 'sizes: ' + x_dim[1] + ' ' + y_dim[1] + ' ' + z_dim[1] + '\n'
        nhdr[4] = 'spacings: ' + x_spacing[1] + ' ' + y_spacing[1] + ' ' + z_spacing[1] + '\n'
        nhdr[5] = 'encoding: raw' + '\n'
        nhdr[6] = 'data file: ' + base + '\n'
        nhdr[7] = 'endian: little' + '\n' 

        # save list as lines to the new file
        save_file, _ = qtw.QFileDialog.getSaveFileName(self)
        file = open(save_file + '.nhdr', "w+")
        file.writelines(nhdr)
        file.close()
        

# Start main loop and exit when quit signal
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())