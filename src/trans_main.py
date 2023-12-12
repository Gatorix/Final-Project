from PySide6.QtCore import Slot, QDir, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QStyle, QLineEdit, QMessageBox

from src.subtitles.extract_text import extract_text_between_bracket
from src.threads.main_thread import MainThread
from src.ui.ui_transub import Ui_MainForm
from src.trans_sub_custom_info import CustomInfoWindow
from src.utils.files import resource_path, get_parent_path
from src.utils.yml import Yml, logger


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        icon = QIcon()
        icon.addFile(resource_path(fr'{get_parent_path()}\\icon\\qtforpython.ico'), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

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

        self.ui.combo_box_convert.currentTextChanged.connect(self.on_convert_combo_changed)

        self.ui.toolButton_add.clicked.connect(self.on_tool_button_add_clicked)
        self.ui.toolButton_remove.clicked.connect(self.on_tool_button_remove_clicked)

        self.ui.button_start.clicked.connect(self.on_start_clicked)
        self.ui.button_cancel.clicked.connect(self.on_cancel_clicked)

        self.main_thread.finished.connect(self.set_start_button_to_enable)

    @Slot()
    def on_convert_combo_changed(self):
        if 'srt' in self.ui.combo_box_convert.currentText():
            self.ui.combo_box_custom_info.setDisabled(True)

        elif 'txt' in self.ui.combo_box_convert.currentText():
            self.ui.combo_box_custom_info.setDisabled(True)
            self.ui.line_edit_offset.setDisabled(True)

        else:
            self.ui.combo_box_custom_info.setEnabled(True)
            self.ui.line_edit_offset.setEnabled(True)

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
    def set_process_max_range(self, value):
        self.ui.progress_bar.setMaximum(value)

    @Slot()
    def reset_process_bar(self):
        self.ui.progress_bar.reset()

    @Slot()
    def set_start_button_to_disable(self):
        self.is_running = True
        self.ui.button_start.setDisabled(True)

    @Slot()
    def set_start_button_to_enable(self):
        self.is_running = False
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
                    self,
                    'Question',
                    'Convert task is still running, Are you sure you want to exit?'
            ) == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()

    @Slot()
    def no_subtitle_files_alert(self):
        QMessageBox.warning(
            self,
            'Warning',
            'There is no subtitle file in the given path.'
        )

    @Slot()
    def print_status_to_label(self, status):
        self.ui.label_status.setText(status)

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

            convert_chinese_kv = {
                'To Simplified': 't2s',
                'To Traditional': 's2t',
                'Disable': None
            }

            self.main_thread.subtitle_path = self.ui.line_edit_path.text()
            self.main_thread.is_archive = self.ui.check_box_archive.isChecked()
            self.main_thread.is_ignore = self.ui.check_box_ignore_error.isChecked()
            self.main_thread.is_ori_encoding = self.ui.check_box_is_original_encoding.isChecked()
            self.main_thread.encoding = extract_text_between_bracket(self.ui.combo_box_encoding.currentText())
            self.main_thread.custom_ass_info = Yml().get_specific_details(self.ui.combo_box_custom_info.currentText())
            self.main_thread.convert_chinese = convert_chinese_kv.get(self.ui.combo_box_chinese.currentText())
            self.main_thread.offset = self.ui.line_edit_offset.text()
            self.main_thread.convert_to = self.ui.combo_box_convert.currentText()

            self.set_start_button_to_disable()

            self.main_thread.start()

    @Slot()
    def on_cancel_clicked(self):
        if self.is_running:
            if QMessageBox.question(
                    self, 'Question', 'Convert task is still running, Are you sure you want to cancel?'
            ) == QMessageBox.StandardButton.Yes:
                self.main_thread.terminate()
                self.reset_process_bar()
