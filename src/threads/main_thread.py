from PySide6.QtCore import Signal, QObject, QThread

from src.utils.yml import logger


class Signals(QObject):
    signal_process_value = Signal(int)
    signal_process_max_range = Signal(int)
    signal_process_failed_reason = Signal(str)


class MainThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.log = logger()

        self.subtitle_path = None
        self.is_archive = False
        self.is_ignore = False
        self.is_text = False
        self.encoding = 'utf-8'
        self.custom_ass_info = ''
        self.convert_chinese = ''
        self.offset = 0.0
        self.convert_to = ''

        self.signals = Signals()
        self.signals.signal_process_value.connect(parent.set_progress_bar_value)
        self.signals.signal_process_max_range.connect(parent.set_process_max_range)

    def run(self) -> None:
        self.log.info('Main thread started.')
        self.all_files = self.get_all_subtitle_files()
        self.signals.signal_process_max_range.emit(len(self.all_files))
        for idx, file in self.all_files:
            if self.is_text:
                pass
            else:
                pass
        self.log.info('Main thread finished.')
        self.finished.emit()

    def get_all_subtitle_files(self):
        return []
