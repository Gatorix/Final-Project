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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_SubCustomInfo(object):
    def setupUi(self, SubCustomInfo):
        if not SubCustomInfo.objectName():
            SubCustomInfo.setObjectName(u"SubCustomInfo")
        SubCustomInfo.resize(400, 450)
        self.layoutWidget = QWidget(SubCustomInfo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 410, 158, 32))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_save = QPushButton(self.layoutWidget)
        self.button_save.setObjectName(u"button_save")

        self.gridLayout.addWidget(self.button_save, 0, 0, 1, 1)

        self.button_close = QPushButton(self.layoutWidget)
        self.button_close.setObjectName(u"button_close")

        self.gridLayout.addWidget(self.button_close, 0, 1, 1, 1)

        self.groupBox = QGroupBox(SubCustomInfo)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 381, 361))
        self.plain_text_edit = QPlainTextEdit(self.groupBox)
        self.plain_text_edit.setObjectName(u"plain_text_edit")
        self.plain_text_edit.setGeometry(QRect(10, 20, 361, 331))
        self.groupBox_2 = QGroupBox(SubCustomInfo)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 0, 381, 51))
        self.line_edit_info_name = QLineEdit(self.groupBox_2)
        self.line_edit_info_name.setObjectName(u"line_edit_info_name")
        self.line_edit_info_name.setGeometry(QRect(10, 20, 361, 21))

        self.retranslateUi(SubCustomInfo)

        QMetaObject.connectSlotsByName(SubCustomInfo)
    # setupUi

    def retranslateUi(self, SubCustomInfo):
        SubCustomInfo.setWindowTitle(QCoreApplication.translate("SubCustomInfo", u"Form", None))
        self.button_save.setText(QCoreApplication.translate("SubCustomInfo", u"Save", None))
        self.button_close.setText(QCoreApplication.translate("SubCustomInfo", u"Close", None))
        self.groupBox.setTitle(QCoreApplication.translate("SubCustomInfo", u"Info Details", None))
        self.plain_text_edit.setPlainText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("SubCustomInfo", u"Info Title", None))
    # retranslateUi

