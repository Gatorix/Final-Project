from PySide6.QtCore import Slot, QDir
from PySide6.QtWidgets import QMainWindow, QFileDialog, QStyle, QLineEdit

from src.ui.ui_transub import Ui_MainForm
from src.transub_sub_custom_info import CustomInfoWindow
from src.utils.yml import Yml


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.ui_custom_info = CustomInfoWindow()

        self.refresh_custom_info()

        self._open_folder_action = self.ui.line_edit_path.addAction(
            qApp.style().standardIcon(QStyle.SP_DirOpenIcon),
            QLineEdit.TrailingPosition
        )

        self._open_folder_action.triggered.connect(self.on_open_folder)

        self.ui_custom_info.signal.close_window_single.connect(self.refresh_custom_info)

        self.ui.toolButton_add.clicked.connect(self.on_tool_button_add_clicked)
        self.ui.toolButton_remove.clicked.connect(self.on_tool_button_remove_clicked)

    @Slot()
    def on_tool_button_add_clicked(self):
        self.ui_custom_info.show()

    @Slot()
    def on_tool_button_remove_clicked(self):
        Yml().remove_specific_title(self.ui.combo_box_custom_info.currentText())
        self.refresh_custom_info()

    @Slot()
    def refresh_custom_info(self):
        self.ui.combo_box_custom_info.clear()
        self.ui.combo_box_custom_info.addItems(Yml().get_all_title())

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
