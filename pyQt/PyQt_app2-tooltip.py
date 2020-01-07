#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a tooltip on 
a window and a button.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont    


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 8))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Close the window', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget. After clicking the window will close.')
        btn.clicked.connect(QApplication.instance().quit)
        btn.clicked.connect(self.printing_text)
        btn.resize(btn.sizeHint())
        btn.move(50, 50) 

        le = QLineEdit()
        le.resize(le.sizeHint())
        le.move(100, 100)      
        
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