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
        MainForm.resize(300, 470)
        self.settings_group = QGroupBox(MainForm)
        self.settings_group.setObjectName(u"settings_group")
        self.settings_group.setGeometry(QRect(10, 70, 281, 321))
        self.layoutWidget = QWidget(self.settings_group)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 120, 261, 31))
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

        self.layoutWidget1 = QWidget(self.settings_group)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 261, 101))
        self.gridLayout_9 = QGridLayout(self.layoutWidget1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.check_box_archive = QCheckBox(self.layoutWidget1)
        self.check_box_archive.setObjectName(u"check_box_archive")

        self.gridLayout_9.addWidget(self.check_box_archive, 0, 0, 1, 1)

        self.check_box_ignore_error = QCheckBox(self.layoutWidget1)
        self.check_box_ignore_error.setObjectName(u"check_box_ignore_error")

        self.gridLayout_9.addWidget(self.check_box_ignore_error, 1, 0, 1, 1)

        self.check_box_extract_text = QCheckBox(self.layoutWidget1)
        self.check_box_extract_text.setObjectName(u"check_box_extract_text")

        self.gridLayout_9.addWidget(self.check_box_extract_text, 2, 0, 1, 1)

        self.layoutWidget2 = QWidget(self.settings_group)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 200, 211, 31))
        self.gridLayout_5 = QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_chinese = QLabel(self.layoutWidget2)
        self.label_chinese.setObjectName(u"label_chinese")

        self.gridLayout_5.addWidget(self.label_chinese, 0, 0, 1, 1)

        self.combo_box_chinese = QComboBox(self.layoutWidget2)
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.setObjectName(u"combo_box_chinese")

        self.gridLayout_5.addWidget(self.combo_box_chinese, 0, 1, 1, 1)

        self.layoutWidget3 = QWidget(self.settings_group)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 280, 161, 31))
        self.gridLayout = QGridLayout(self.layoutWidget3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_convert = QLabel(self.layoutWidget3)
        self.label_convert.setObjectName(u"label_convert")

        self.gridLayout.addWidget(self.label_convert, 0, 0, 1, 1)

        self.combo_box_convert = QComboBox(self.layoutWidget3)
        self.combo_box_convert.addItem("")
        self.combo_box_convert.addItem("")
        self.combo_box_convert.setObjectName(u"combo_box_convert")

        self.gridLayout.addWidget(self.combo_box_convert, 0, 1, 1, 1)

        self.layoutWidget4 = QWidget(self.settings_group)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 240, 171, 31))
        self.gridLayout_4 = QGridLayout(self.layoutWidget4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_offset = QLabel(self.layoutWidget4)
        self.label_offset.setObjectName(u"label_offset")

        self.gridLayout_4.addWidget(self.label_offset, 0, 0, 1, 1)

        self.line_edit_offset = QLineEdit(self.layoutWidget4)
        self.line_edit_offset.setObjectName(u"line_edit_offset")

        self.gridLayout_4.addWidget(self.line_edit_offset, 0, 1, 1, 1)

        self.layoutWidget5 = QWidget(self.settings_group)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(13, 165, 211, 23))
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

        self.toolButton_add = QToolButton(self.settings_group)
        self.toolButton_add.setObjectName(u"toolButton_add")
        self.toolButton_add.setGeometry(QRect(230, 166, 21, 21))
        self.toolButton_remove = QToolButton(self.settings_group)
        self.toolButton_remove.setObjectName(u"toolButton_remove")
        self.toolButton_remove.setEnabled(True)
        self.toolButton_remove.setGeometry(QRect(250, 166, 21, 21))
        self.folder_group = QGroupBox(MainForm)
        self.folder_group.setObjectName(u"folder_group")
        self.folder_group.setGeometry(QRect(10, 0, 281, 71))
        self.layoutWidget6 = QWidget(self.folder_group)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 30, 261, 23))
        self.gridLayout_3 = QGridLayout(self.layoutWidget6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_path = QLabel(self.layoutWidget6)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_3.addWidget(self.label_path, 0, 0, 1, 1)

        self.line_edit_path = QLineEdit(self.layoutWidget6)
        self.line_edit_path.setObjectName(u"line_edit_path")
        self.line_edit_path.setReadOnly(True)

        self.gridLayout_3.addWidget(self.line_edit_path, 0, 1, 1, 1)

        self.button_start = QPushButton(MainForm)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(221, 400, 75, 31))
        self.layoutWidget7 = QWidget(MainForm)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(11, 395, 201, 71))
        self.gridLayout_6 = QGridLayout(self.layoutWidget7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.layoutWidget7)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout_6.addWidget(self.label_status, 0, 0, 1, 1)

        self.progress_bar = QProgressBar(self.layoutWidget7)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setInvertedAppearance(False)

        self.gridLayout_6.addWidget(self.progress_bar, 1, 0, 1, 1)

        self.button_cancel = QPushButton(MainForm)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(221, 434, 75, 31))

        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.settings_group.setTitle(QCoreApplication.translate("MainForm", u"Step 2: Settings", None))
        self.combo_box_encoding.setItemText(0, QCoreApplication.translate("MainForm", u"Unicode (UTF-8)", None))
        self.combo_box_encoding.setItemText(1, QCoreApplication.translate("MainForm", u"Unicode (UTF-16)", None))
        self.combo_box_encoding.setItemText(2, QCoreApplication.translate("MainForm", u"Simplified Chinese (GB18030)", None))
        self.combo_box_encoding.setItemText(3, QCoreApplication.translate("MainForm", u"Traditional Chinese (Big5)", None))
        self.combo_box_encoding.setItemText(4, QCoreApplication.translate("MainForm", u"Japanese (Shift-JIS)", None))

        self.label_encoding.setText(QCoreApplication.translate("MainForm", u"Encoding", None))
        self.check_box_archive.setText(QCoreApplication.translate("MainForm", u"Archive Results Into Single ZIP File", None))
        self.check_box_ignore_error.setText(QCoreApplication.translate("MainForm", u"Ignore Encoding Errors", None))
        self.check_box_extract_text.setText(QCoreApplication.translate("MainForm", u"Extract Plain Text", None))
        self.label_chinese.setText(QCoreApplication.translate("MainForm", u"Convert Chinese", None))
        self.combo_box_chinese.setItemText(0, QCoreApplication.translate("MainForm", u"Disable", None))
        self.combo_box_chinese.setItemText(1, QCoreApplication.translate("MainForm", u"To Simplified", None))
        self.combo_box_chinese.setItemText(2, QCoreApplication.translate("MainForm", u"To Traditional", None))

        self.label_convert.setText(QCoreApplication.translate("MainForm", u"Convert to", None))
        self.combo_box_convert.setItemText(0, QCoreApplication.translate("MainForm", u"*.ass", None))
        self.combo_box_convert.setItemText(1, QCoreApplication.translate("MainForm", u"*.srt", None))

        self.label_offset.setText(QCoreApplication.translate("MainForm", u"Subtitle Offset ", None))
        self.line_edit_offset.setText("")
        self.line_edit_offset.setPlaceholderText(QCoreApplication.translate("MainForm", u"0.0", None))
        self.label_chinese_2.setText(QCoreApplication.translate("MainForm", u"Custom *.ass Info", None))
        self.combo_box_custom_info.setItemText(0, QCoreApplication.translate("MainForm", u"None", None))

        self.toolButton_add.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.toolButton_remove.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.folder_group.setTitle(QCoreApplication.translate("MainForm", u"Step 1: Select File Path", None))
        self.label_path.setText(QCoreApplication.translate("MainForm", u"Path", None))
        self.button_start.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.label_status.setText(QCoreApplication.translate("MainForm", u"Click \"Start\" when you're ready.", None))
        self.button_cancel.setText(QCoreApplication.translate("MainForm", u"Cancel", None))
    # retranslateUi

