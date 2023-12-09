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

    def run(self) -> None:
        self.log.info('Main thread started.')
