from PySide6.QtCore import Slot, QObject, Signal
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.ui.ui_transub_custom_info import Ui_SubCustomInfo
from src.utils.yml import Yml, logger

DEFAULT_INFO = '''[Script Info]
; This is a Sub Station Alpha v4 script.
Title: Neon Genesis Evangelion - Episode 26
Original Script: RoRo
Script Updated By: version 2.8.01
ScriptType: v4.00
Collisions: Normal
PlayResY: 600
PlayDepth: 0
Timer: 100,0000

[V4 Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, AlphaLevel, Encoding
Style: DefaultVCD, Arial,28,11861244,11861244,11861244,-2147483640,-1,0,1,1,2,2,30,30,30,0,0
'''


class InfoWindowClose(QObject):
    close_window_single = Signal()


class CustomInfoWindow(QMainWindow):
    def __init__(self):
        super(CustomInfoWindow, self).__init__()
        self.ui = Ui_SubCustomInfo()
        self.ui.setupUi(self)

        self.log = logger()

        self.signal = InfoWindowClose()

        self.is_changed = False

        self.ui.plain_text_edit.setPlaceholderText(DEFAULT_INFO)

        self.ui.plain_text_edit.textChanged.connect(self.on_text_change)
        self.ui.line_edit_info_name.textChanged.connect(self.on_text_change)
        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_save.clicked.connect(self.on_save)

    @Slot()
    def on_text_change(self):
        self.is_changed = True

    @Slot()
    def closeEvent(self, event):
        if self.is_changed:
            if QMessageBox.question(
                    self, 'Question', 'The info is not saved, are you sure to close it?'
            ) == QMessageBox.StandardButton.Yes:
                event.accept()
                self.reset_text_edit()
            else:
                event.ignore()
        else:
            event.accept()
            self.reset_text_edit()

    @Slot()
    def on_save(self):
        if not self.ui.line_edit_info_name.text():
            self.log.warning('Please enter the info name.')
            QMessageBox.warning(
                self, 'Warning', 'Please enter the info name.'
            )

        elif any(['[Script Info]' not in self.ui.plain_text_edit.toPlainText(),
                  '[V4 Styles]' not in self.ui.plain_text_edit.toPlainText()]):
            self.log.warning('Info must contains [Script Info] and [V4 Styles] labels.')
            QMessageBox.warning(
                self, 'Warning', 'Info must contains [Script Info] and [V4 Styles] labels.'
            )

        else:
            save_result = self.save_info_to_yml(
                self.ui.line_edit_info_name.text(),
                self.ui.plain_text_edit.toPlainText()
            )
            if save_result.get('result'):
                self.is_changed = False
                self.close()
                self.log.info('Info save successful.')
            else:
                self.log.error(f'Info save failed. Cause {save_result.get("msg")}')
                QMessageBox.warning(
                    self,
                    'Warning',
                    save_result.get('msg')
                )
        self.signal.close_window_single.emit()

    def reset_text_edit(self):
        self.ui.line_edit_info_name.clear()
        self.ui.plain_text_edit.clear()
        self.is_changed = False

    @staticmethod
    def save_info_to_yml(title, info):
        return Yml().write_info_to_yml(title, info)
