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
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 450)
        self.settings_group = QGroupBox(Form)
        self.settings_group.setObjectName(u"settings_group")
        self.settings_group.setGeometry(QRect(10, 90, 281, 281))
        self.widget = QWidget(self.settings_group)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 120, 257, 31))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.combo_box_encoding = QComboBox(self.widget)
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.addItem("")
        self.combo_box_encoding.setObjectName(u"combo_box_encoding")

        self.gridLayout_2.addWidget(self.combo_box_encoding, 0, 1, 1, 1)

        self.label_encoding = QLabel(self.widget)
        self.label_encoding.setObjectName(u"label_encoding")

        self.gridLayout_2.addWidget(self.label_encoding, 0, 0, 1, 1)

        self.widget1 = QWidget(self.settings_group)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 20, 261, 101))
        self.gridLayout_9 = QGridLayout(self.widget1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.check_box_archive = QCheckBox(self.widget1)
        self.check_box_archive.setObjectName(u"check_box_archive")

        self.gridLayout_9.addWidget(self.check_box_archive, 0, 0, 1, 1)

        self.check_box_ignore_error = QCheckBox(self.widget1)
        self.check_box_ignore_error.setObjectName(u"check_box_ignore_error")

        self.gridLayout_9.addWidget(self.check_box_ignore_error, 1, 0, 1, 1)

        self.check_box_extract_text = QCheckBox(self.widget1)
        self.check_box_extract_text.setObjectName(u"check_box_extract_text")

        self.gridLayout_9.addWidget(self.check_box_extract_text, 2, 0, 1, 1)

        self.widget2 = QWidget(self.settings_group)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 200, 191, 31))
        self.gridLayout_5 = QGridLayout(self.widget2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_chinese = QLabel(self.widget2)
        self.label_chinese.setObjectName(u"label_chinese")

        self.gridLayout_5.addWidget(self.label_chinese, 0, 0, 1, 1)

        self.combo_box_chinese = QComboBox(self.widget2)
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.addItem("")
        self.combo_box_chinese.setObjectName(u"combo_box_chinese")

        self.gridLayout_5.addWidget(self.combo_box_chinese, 0, 1, 1, 1)

        self.widget3 = QWidget(self.settings_group)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 240, 122, 31))
        self.gridLayout = QGridLayout(self.widget3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_convert = QLabel(self.widget3)
        self.label_convert.setObjectName(u"label_convert")

        self.gridLayout.addWidget(self.label_convert, 0, 0, 1, 1)

        self.combo_box_convert = QComboBox(self.widget3)
        self.combo_box_convert.addItem("")
        self.combo_box_convert.addItem("")
        self.combo_box_convert.setObjectName(u"combo_box_convert")

        self.gridLayout.addWidget(self.combo_box_convert, 0, 1, 1, 1)

        self.button_custom = QPushButton(self.settings_group)
        self.button_custom.setObjectName(u"button_custom")
        self.button_custom.setGeometry(QRect(164, 240, 111, 31))
        self.widget4 = QWidget(self.settings_group)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(10, 160, 201, 31))
        self.gridLayout_4 = QGridLayout(self.widget4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_offset = QLabel(self.widget4)
        self.label_offset.setObjectName(u"label_offset")

        self.gridLayout_4.addWidget(self.label_offset, 0, 0, 1, 1)

        self.line_edit_offset = QLineEdit(self.widget4)
        self.line_edit_offset.setObjectName(u"line_edit_offset")

        self.gridLayout_4.addWidget(self.line_edit_offset, 0, 1, 1, 1)

        self.folder_group = QGroupBox(Form)
        self.folder_group.setObjectName(u"folder_group")
        self.folder_group.setGeometry(QRect(10, 10, 281, 71))
        self.widget5 = QWidget(self.folder_group)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(10, 30, 261, 23))
        self.gridLayout_3 = QGridLayout(self.widget5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_path = QLabel(self.widget5)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_3.addWidget(self.label_path, 0, 0, 1, 1)

        self.line_edit_path = QLineEdit(self.widget5)
        self.line_edit_path.setObjectName(u"line_edit_path")

        self.gridLayout_3.addWidget(self.line_edit_path, 0, 1, 1, 1)

        self.widget6 = QWidget(Form)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(10, 380, 281, 61))
        self.gridLayout_6 = QGridLayout(self.widget6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.widget6)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout_6.addWidget(self.label_status, 0, 0, 1, 1)

        self.button_start = QPushButton(self.widget6)
        self.button_start.setObjectName(u"button_start")

        self.gridLayout_6.addWidget(self.button_start, 0, 1, 1, 1)

        self.progress_bar = QProgressBar(self.widget6)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setValue(24)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setInvertedAppearance(False)

        self.gridLayout_6.addWidget(self.progress_bar, 1, 0, 1, 1)

        self.button_cancel = QPushButton(self.widget6)
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

        self.button_custom.setText(QCoreApplication.translate("Form", u"Custom Style", None))
        self.label_offset.setText(QCoreApplication.translate("Form", u"Subtitle Offset ", None))
        self.line_edit_offset.setText("")
        self.line_edit_offset.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.folder_group.setTitle(QCoreApplication.translate("Form", u"Step 1: Select folder", None))
        self.label_path.setText(QCoreApplication.translate("Form", u"Source Path", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"Click \"Start\" when you're ready.", None))
        self.button_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.button_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

