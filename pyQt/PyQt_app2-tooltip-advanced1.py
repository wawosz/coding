#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QLineEdit, QPushButton,
                             QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 8))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.le = QLineEdit(self)
        self.le.setText('Text within the QLineEdit')
        self.le.resize(self.le.sizeHint())
        self.le.move(100, 100)

        btn = QPushButton('Close the window', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget. After clicking, \
            the window will close.')

        btn.clicked.connect(self.printing_text)
        btn.clicked.connect(QApplication.instance().quit)

        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    def printing_text(self):
        print('button clicked and window closed!!!')
        print(self.le.text())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
