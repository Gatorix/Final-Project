# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transub.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 470)
        self.settings_group = QGroupBox(Form)
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
        self.layoutWidget2.setGeometry(QRect(10, 200, 245, 31))
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

        self.widget = QWidget(self.settings_group)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 160, 261, 31))
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_chinese_2 = QLabel(self.widget)
        self.label_chinese_2.setObjectName(u"label_chinese_2")

        self.gridLayout_7.addWidget(self.label_chinese_2, 0, 0, 1, 1)

        self.combo_box_chinese_2 = QComboBox(self.widget)
        self.combo_box_chinese_2.addItem("")
        self.combo_box_chinese_2.setObjectName(u"combo_box_chinese_2")

        self.gridLayout_7.addWidget(self.combo_box_chinese_2, 0, 1, 1, 1)

        self.toolButton = QToolButton(self.widget)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_7.addWidget(self.toolButton, 0, 2, 1, 1)

        self.folder_group = QGroupBox(Form)
        self.folder_group.setObjectName(u"folder_group")
        self.folder_group.setGeometry(QRect(10, 0, 281, 71))
        self.layoutWidget5 = QWidget(self.folder_group)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 30, 261, 23))
        self.gridLayout_3 = QGridLayout(self.layoutWidget5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_path = QLabel(self.layoutWidget5)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_3.addWidget(self.label_path, 0, 0, 1, 1)

        self.line_edit_path = QLineEdit(self.layoutWidget5)
        self.line_edit_path.setObjectName(u"line_edit_path")
        self.line_edit_path.setReadOnly(True)

        self.gridLayout_3.addWidget(self.line_edit_path, 0, 1, 1, 1)

        self.layoutWidget6 = QWidget(Form)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 400, 285, 66))
        self.gridLayout_6 = QGridLayout(self.layoutWidget6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.layoutWidget6)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout_6.addWidget(self.label_status, 0, 0, 1, 1)

        self.button_start = QPushButton(self.layoutWidget6)
        self.button_start.setObjectName(u"button_start")

        self.gridLayout_6.addWidget(self.button_start, 0, 1, 1, 1)

        self.progress_bar = QProgressBar(self.layoutWidget6)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setValue(24)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setInvertedAppearance(False)

        self.gridLayout_6.addWidget(self.progress_bar, 1, 0, 1, 1)

        self.button_cancel = QPushButton(self.layoutWidget6)
        self.button_cancel.setObjectName(u"button_cancel")

        self.gridLayout_6.addWidget(self.button_cancel, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settings_group.setTitle(QCoreApplication.translate("Form", u"Step 2: Settings", None))
        self.combo_box_encoding.setItemText(0, QCoreApplication.translate("Form", u"Unicode (UTF-8)", None))
        self.combo_box_encoding.setItemText(1, QCoreApplication.translate("Form", u"Unicode (UTF-16)", None))
        self.combo_box_encoding.setItemText(2, QCoreApplication.translate("Form", u"Simplified Chinese (GB18030)", None))
        self.combo_box_encoding.setItemText(3, QCoreApplication.translate("Form", u"Traditional Chinese (Big5)", None))
        self.combo_box_encoding.setItemText(4, QCoreApplication.translate("Form", u"Japanese (Shift-JIS)", None))

        self.label_encoding.setText(QCoreApplication.translate("Form", u"Encoding", None))
        self.check_box_archive.setText(QCoreApplication.translate("Form", u"Archive Results Into Single ZIP File", None))
        self.check_box_ignore_error.setText(QCoreApplication.translate("Form", u"Ignore Encoding Errors", None))
        self.check_box_extract_text.setText(QCoreApplication.translate("Form", u"Extract Plain Text", None))
        self.label_chinese.setText(QCoreApplication.translate("Form", u"Convert Chinese", None))
        self.combo_box_chinese.setItemText(0, QCoreApplication.translate("Form", u"Disable", None))
        self.combo_box_chinese.setItemText(1, QCoreApplication.translate("Form", u"To Simplified", None))
        self.combo_box_chinese.setItemText(2, QCoreApplication.translate("Form", u"To Traditional", None))

        self.label_convert.setText(QCoreApplication.translate("Form", u"Convert to", None))
        self.combo_box_convert.setItemText(0, QCoreApplication.translate("Form", u"*.ass", None))
        self.combo_box_convert.setItemText(1, QCoreApplication.translate("Form", u"*.srt", None))

        self.label_offset.setText(QCoreApplication.translate("Form", u"Subtitle Offset ", None))
        self.line_edit_offset.setText("")
        self.line_edit_offset.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_chinese_2.setText(QCoreApplication.translate("Form", u"Custom *.ass Info", None))
        self.combo_box_chinese_2.setItemText(0, QCoreApplication.translate("Form", u"None", None))

        self.toolButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.folder_group.setTitle(QCoreApplication.translate("Form", u"Step 1: Select folder", None))
        self.label_path.setText(QCoreApplication.translate("Form", u"Source Path", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"Click \"Start\" when you're ready.", None))
        self.button_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.button_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

