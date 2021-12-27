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
        self.width = 320
        self.height = 240
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Define widgets
        self.load_label = qtw.QLabel('Load *.hdr file to convert')
        self.load_button = qtw.QPushButton('LOAD')

        self.convert_label = qtw.QLabel('Save converted file as')
        self.convert_button = qtw.QPushButton('CONVERT')
        #convert_button.setFont(qtg.QFont('Bold', 13))

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
        fname, _ = qtw.QFileDialog.getOpenFileName(self,'Open Inveon header (*.hdr) file to convert', 'c:\\',"Header file (*.hdr)")
        if fname:
            print(fname)

    # Method: print info and convert file
    def convert_file(self):
        self.info_text.setPlainText("PASS1\nPASS2")
        print('PASS')

# Start main loop and exit when quit signal
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())