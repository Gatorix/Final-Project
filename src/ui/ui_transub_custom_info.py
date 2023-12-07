# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transub_custom_info.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 10, 381, 241))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 260, 158, 31))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u" [Script Info]\n"
" ; This is a Sub Station Alpha v4 script.\n"
" ; For Sub Station Alpha info and downloads,\n"
" ; go to http://www.eswat.demon.co.uk/\n"
" Title: Neon Genesis Evangelion - Episode 26 (neutral Spanish)\n"
" Original Script: RoRo\n"
" Script Updated By: version 2.8.01\n"
" ScriptType: v4.00\n"
" Collisions: Normal\n"
" PlayResY: 600\n"
" PlayDepth: 0\n"
" Timer: 100,0000\n"
"  \n"
" [V4 Styles]\n"
" Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, \n"
"    Alignment, MarginL, MarginR, MarginV, AlphaLevel, Encoding\n"
" Style: DefaultVCD, Arial,28,11861244,11861244,11861244,-2147483640,-1,0,1,1,2,2,30,30,30,0,0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

