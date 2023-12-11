import time

from PySide6.QtCore import Signal, QObject, QThread

from src.subtitles.extract_text import extract_plain_text
from src.utils.times import get_current_milli_time
from src.utils.yml import logger
from src.utils.files import get_all_filepath


class Signals(QObject):
    signal_no_subtitle_files = Signal()
    signal_process_value = Signal(int)
    signal_process_max_range = Signal(int)
    signal_status = Signal(str)


class MainThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.log = logger()

        self.subtitle_path = None
        self.all_files = None
        self.is_archive = False
        self.is_ignore = False
        self.is_ori_encoding = False
        self.encoding = None
        self.custom_ass_info = ''
        self.convert_chinese = ''
        self.offset = 0.0
        self.convert_to = ''
        self.output_file_path = None

        self.signals = Signals()
        self.signals.signal_no_subtitle_files.connect(parent.no_subtitle_files_alert)
        self.signals.signal_process_value.connect(parent.set_progress_bar_value)
        self.signals.signal_process_max_range.connect(parent.set_process_max_range)
        self.signals.signal_status.connect(parent.print_status_to_label)

    def run(self) -> None:
        self.log.info('Main thread started.')
        self.all_files = get_all_filepath(self.subtitle_path)
        self.output_file_path = f'./result_{get_current_milli_time()}'

        if not self.all_files:
            self.signals.signal_no_subtitle_files.emit()
        else:
            self.signals.signal_process_max_range.emit(len(self.all_files))

            for idx, file in enumerate(self.all_files):
                self.log.info(f'processing {file}')
                if 'txt' in self.convert_to:
                    self.log.info(f'txt')
                    result = extract_plain_text(
                        file,
                        output_file_path=self.output_file_path,
                        is_ignore=self.is_ignore,
                        is_ori_encoding=self.is_ori_encoding,
                        specified_encoding=self.encoding
                    )
                    if not result.get('result'):
                        self.log.error(result.get('msg'))
                    self.signals.signal_status.emit(result.get('msg'))

                else:
                    pass

                self.signals.signal_process_value.emit(idx + 1)

        self.log.info('Main thread finished.')
        self.finished.emit()
