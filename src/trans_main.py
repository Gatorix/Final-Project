from PySide6.QtCore import Slot, QDir
from PySide6.QtWidgets import QMainWindow, QFileDialog, QStyle, QLineEdit, QMessageBox

from src.threads.main_thread import MainThread
from src.ui.ui_transub import Ui_MainForm
from src.trans_sub_custom_info import CustomInfoWindow
from src.utils.yml import Yml, logger


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.log = logger()

        self.is_running = False

        self.ui_custom_info = CustomInfoWindow()
        self.main_thread = MainThread(self)

        self.refresh_custom_info()

        self._open_folder_action = self.ui.line_edit_path.addAction(
            qApp.style().standardIcon(QStyle.SP_DirOpenIcon),
            QLineEdit.TrailingPosition
        )

        self._open_folder_action.triggered.connect(self.on_open_folder)

        self.ui_custom_info.signal.close_window_single.connect(self.refresh_custom_info)

        self.ui.check_box_extract_text.clicked.connect(self.on_extract_text_clicked)
        self.ui.combo_box_convert.currentTextChanged.connect(self.on_convert_combo_changed)

        self.ui.toolButton_add.clicked.connect(self.on_tool_button_add_clicked)
        self.ui.toolButton_remove.clicked.connect(self.on_tool_button_remove_clicked)

        self.ui.button_start.clicked.connect(self.on_start_clicked)

    @Slot()
    def on_extract_text_clicked(self):
        if self.ui.check_box_extract_text.isChecked():
            self.ui.combo_box_custom_info.setDisabled(True)
            self.ui.line_edit_offset.setDisabled(True)
            self.ui.combo_box_convert.setDisabled(True)
        else:
            if 'srt' not in self.ui.combo_box_convert.currentText():
                self.ui.combo_box_custom_info.setEnabled(True)
            self.ui.combo_box_convert.setEnabled(True)
            self.ui.line_edit_offset.setEnabled(True)

    @Slot()
    def on_convert_combo_changed(self):
        if 'srt' in self.ui.combo_box_convert.currentText():
            self.ui.combo_box_custom_info.setDisabled(True)
        else:
            self.ui.combo_box_custom_info.setEnabled(True)

    @Slot()
    def on_tool_button_add_clicked(self):
        self.ui_custom_info.show()

    @Slot()
    def on_tool_button_remove_clicked(self):
        Yml().remove_specific_title(self.ui.combo_box_custom_info.currentText())
        self.refresh_custom_info()

    @Slot()
    def refresh_custom_info(self):
        if len(Yml().get_all_title()):
            self.ui.combo_box_custom_info.clear()
            self.ui.combo_box_custom_info.addItems(Yml().get_all_title())
        else:
            self.ui.combo_box_custom_info.clear()
            self.ui.combo_box_custom_info.addItem('None')

    @Slot()
    def set_progress_bar_value(self, value):
        self.ui.progress_bar.setValue(value)

    @Slot()
    def set_running_status_to_true(self):
        self.is_running = True

    @Slot()
    def set_running_status_to_false(self):
        self.is_running = False

    @Slot()
    def set_start_button_to_disable(self):
        self.ui.button_start.setDisabled(True)

    @Slot()
    def set_start_button_to_enable(self):
        self.ui.button_start.setEnabled(True)

    @Slot()
    def on_open_folder(self):
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Open Directory",
            # QDir.homePath(),
            './',
            QFileDialog.ShowDirsOnly
        )

        if dir_path:
            choose_dir = QDir(dir_path)
            self.ui.line_edit_path.setText(QDir.fromNativeSeparators(choose_dir.path()))

    @Slot()
    def closeEvent(self, event):
        if self.is_running:
            if QMessageBox.question(
                    self, 'Question', 'Convert task is still running, Are you sure you want to exit?'
            ) == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()

    @Slot()
    def on_start_clicked(self):
        if not self.ui.line_edit_path.text():
            self.log.warning('Please Select The File Path First.')
            QMessageBox.warning(
                self,
                'Warning',
                'Please Select The File Path First.'
            )
        else:
            self.log.info('Init the main thread.')
            self.main_thread.is_archive = self.ui.check_box_archive
            self.main_thread.is_ignore = self.ui.check_box_ignore_error
            self.main_thread.is_text = self.ui.check_box_extract_text
            self.main_thread.encoding = self.ui.combo_box_encoding
            self.main_thread.custom_ass_info = Yml().get_specific_details(self.ui.combo_box_custom_info.currentText())
            self.main_thread.convert_chinese = self.ui.combo_box_chinese.currentText()
            self.main_thread.offset = self.ui.line_edit_offset.text()
            self.main_thread.convert_to = self.ui.combo_box_convert.currentText()

            self.set_running_status_to_true()
            self.set_start_button_to_disable()

            self.main_thread.start()

    @Slot()
    def on_cancel_clicked(self):
        if self.is_running:
            if QMessageBox.question(
                    self, 'Question', 'Convert task is still running, Are you sure you want to cancel?'
            ) == QMessageBox.StandardButton.Yes:
                pass
                # TODO
            else:
                pass
                # TODO
