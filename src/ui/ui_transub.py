# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transub.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QToolButton, QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(300, 480)
        MainForm.setMinimumSize(QSize(300, 480))
        MainForm.setMaximumSize(QSize(300, 480))
        self.settings_group = QGroupBox(MainForm)
        self.settings_group.setObjectName(u"settings_group")
        self.settings_group.setGeometry(QRect(10, 70, 281, 111))
        self.layoutWidget = QWidget(self.settings_group)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 261, 31))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.combo_box_encoding = QComboBox(self.layoutWidget)
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.setObjectName(u"combo_box_encoding")

        self.gridLayout_2.addWidget(self.combo_box_encoding, 0, 1, 1, 1)

        self.label_encoding = QLabel(self.layoutWidget)
        self.label_encoding.setObjectName(u"label_encoding")

        self.gridLayout_2.addWidget(self.label_encoding, 0, 0, 1, 1)

        self.check_box_is_original_encoding = QCheckBox(self.settings_group)
        self.check_box_is_original_encoding.setObjectName(u"check_box_is_original_encoding")
        self.check_box_is_original_encoding.setGeometry(QRect(10, 50, 201, 16))
        self.check_box_is_original_encoding.setChecked(True)
        self.check_box_ignore_error = QCheckBox(self.settings_group)
        self.check_box_ignore_error.setObjectName(u"check_box_ignore_error")
        self.check_box_ignore_error.setGeometry(QRect(10, 20, 155, 16))
        self.check_box_ignore_error.setChecked(True)
        self.folder_group = QGroupBox(MainForm)
        self.folder_group.setObjectName(u"folder_group")
        self.folder_group.setGeometry(QRect(10, 10, 281, 51))
        self.layoutWidget1 = QWidget(self.folder_group)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 261, 23))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_path = QLabel(self.layoutWidget1)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_3.addWidget(self.label_path, 0, 0, 1, 1)

        self.line_edit_path = QLineEdit(self.layoutWidget1)
        self.line_edit_path.setObjectName(u"line_edit_path")
        self.line_edit_path.setReadOnly(True)

        self.gridLayout_3.addWidget(self.line_edit_path, 0, 1, 1, 1)

        self.button_start = QPushButton(MainForm)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(220, 410, 71, 31))
        self.layoutWidget2 = QWidget(MainForm)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(11, 400, 201, 71))
        self.gridLayout_6 = QGridLayout(self.layoutWidget2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.layoutWidget2)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout_6.addWidget(self.label_status, 0, 0, 1, 1)

        self.progress_bar = QProgressBar(self.layoutWidget2)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setInvertedAppearance(False)

        self.gridLayout_6.addWidget(self.progress_bar, 1, 0, 1, 1)

        self.button_cancel = QPushButton(MainForm)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(220, 440, 71, 31))
        self.groupBox = QGroupBox(MainForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 190, 281, 211))
        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 100, 171, 31))
        self.gridLayout_4 = QGridLayout(self.layoutWidget3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_offset = QLabel(self.layoutWidget3)
        self.label_offset.setObjectName(u"label_offset")

        self.gridLayout_4.addWidget(self.label_offset, 0, 0, 1, 1)

        self.line_edit_offset = QLineEdit(self.layoutWidget3)
        self.line_edit_offset.setObjectName(u"line_edit_offset")

        self.gridLayout_4.addWidget(self.line_edit_offset, 0, 1, 1, 1)

        self.layoutWidget4 = QWidget(self.groupBox)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 60, 211, 31))
        self.gridLayout_5 = QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_chinese = QLabel(self.layoutWidget4)
        self.label_chinese.setObjectName(u"label_chinese")

        self.gridLayout_5.addWidget(self.label_chinese, 0, 0, 1, 1)

        self.combo_box_chinese = QComboBox(self.layoutWidget4)
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.setObjectName(u"combo_box_chinese")

        self.gridLayout_5.addWidget(self.combo_box_chinese, 0, 1, 1, 1)

        self.layoutWidget5 = QWidget(self.groupBox)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 20, 211, 31))
        self.gridLayout_7 = QGridLayout(self.layoutWidget5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_chinese_2 = QLabel(self.layoutWidget5)
        self.label_chinese_2.setObjectName(u"label_chinese_2")

        self.gridLayout_7.addWidget(self.label_chinese_2, 0, 0, 1, 1)

        self.combo_box_custom_info = QComboBox(self.layoutWidget5)
        self.combo_box_custom_info.addItem("")
        self.combo_box_custom_info.setObjectName(u"combo_box_custom_info")

        self.gridLayout_7.addWidget(self.combo_box_custom_info, 0, 1, 1, 1)

        self.layoutWidget6 = QWidget(self.groupBox)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 140, 161, 31))
        self.gridLayout = QGridLayout(self.layoutWidget6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_convert = QLabel(self.layoutWidget6)
        self.label_convert.setObjectName(u"label_convert")

        self.gridLayout.addWidget(self.label_convert, 0, 0, 1, 1)

        self.combo_box_convert = QComboBox(self.layoutWidget6)
        self.combo_box_convert.addItem("")
        self.combo_box_convert.addItem("")
        self.combo_box_convert.addItem("")
        self.combo_box_convert.setObjectName(u"combo_box_convert")

        self.gridLayout.addWidget(self.combo_box_convert, 0, 1, 1, 1)

        self.check_box_archive = QCheckBox(self.groupBox)
        self.check_box_archive.setObjectName(u"check_box_archive")
        self.check_box_archive.setGeometry(QRect(10, 180, 239, 16))
        self.layoutWidget7 = QWidget(self.groupBox)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(230, 19, 41, 31))
        self.gridLayout_8 = QGridLayout(self.layoutWidget7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toolButton_add = QToolButton(self.layoutWidget7)
        self.toolButton_add.setObjectName(u"toolButton_add")

        self.gridLayout_8.addWidget(self.toolButton_add, 0, 0, 1, 1)

        self.toolButton_remove = QToolButton(self.layoutWidget7)
        self.toolButton_remove.setObjectName(u"toolButton_remove")
        self.toolButton_remove.setEnabled(True)

        self.gridLayout_8.addWidget(self.toolButton_remove, 0, 1, 1, 1)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.settings_group.setTitle(QCoreApplication.translate("MainForm", u"Encode Settings", None))
        self.combo_box_encoding.setItemText(0, QCoreApplication.translate("MainForm", u"Unicode (UTF-8)", None))
        self.combo_box_encoding.setItemText(1, QCoreApplication.translate("MainForm", u"Unicode (UTF-16)", None))
        self.combo_box_encoding.setItemText(2, QCoreApplication.translate("MainForm", u"Simplified Chinese (GB18030)", None))
        self.combo_box_encoding.setItemText(3, QCoreApplication.translate("MainForm", u"Traditional Chinese (Big5)", None))
        self.combo_box_encoding.setItemText(4, QCoreApplication.translate("MainForm", u"Japanese (Shift-JIS)", None))

        self.label_encoding.setText(QCoreApplication.translate("MainForm", u"Encoding", None))
        self.check_box_is_original_encoding.setText(QCoreApplication.translate("MainForm", u"Use the original file encoding", None))
        self.check_box_ignore_error.setText(QCoreApplication.translate("MainForm", u"Ignore Encoding Errors", None))
        self.folder_group.setTitle(QCoreApplication.translate("MainForm", u"Select File Path", None))
        self.label_path.setText(QCoreApplication.translate("MainForm", u"Path", None))
        self.button_start.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.label_status.setText(QCoreApplication.translate("MainForm", u"Click \"Start\" when you're ready.", None))
        self.button_cancel.setText(QCoreApplication.translate("MainForm", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainForm", u"Subtitle Settings", None))
        self.label_offset.setText(QCoreApplication.translate("MainForm", u"Subtitle Offset ", None))
        self.line_edit_offset.setText("")
        self.line_edit_offset.setPlaceholderText(QCoreApplication.translate("MainForm", u"0.0", None))
        self.label_chinese.setText(QCoreApplication.translate("MainForm", u"Convert Chinese", None))
        self.combo_box_chinese.setItemText(0, QCoreApplication.translate("MainForm", u"Disable", None))
        self.combo_box_chinese.setItemText(1, QCoreApplication.translate("MainForm", u"To Simplified", None))
        self.combo_box_chinese.setItemText(2, QCoreApplication.translate("MainForm", u"To Traditional", None))

        self.label_chinese_2.setText(QCoreApplication.translate("MainForm", u"Custom *.ass Info", None))
        self.combo_box_custom_info.setItemText(0, QCoreApplication.translate("MainForm", u"None", None))

        self.label_convert.setText(QCoreApplication.translate("MainForm", u"Convert to", None))
        self.combo_box_convert.setItemText(0, QCoreApplication.translate("MainForm", u"*.ass", None))
        self.combo_box_convert.setItemText(1, QCoreApplication.translate("MainForm", u"*.srt", None))
        self.combo_box_convert.setItemText(2, QCoreApplication.translate("MainForm", u"*.txt", None))

        self.check_box_archive.setText(QCoreApplication.translate("MainForm", u"Archive Results Into Single ZIP File", None))
        self.toolButton_add.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.toolButton_remove.setText(QCoreApplication.translate("MainForm", u"-", None))
    # retranslateUi

