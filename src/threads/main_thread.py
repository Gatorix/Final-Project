from PySide6.QtCore import Signal, QObject, QThread

from src.subtitles.subtitles_converter import convert
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

        self.signals = Signals()
        self.signals.signal_no_subtitle_files.connect(parent.no_subtitle_files_alert)
        self.signals.signal_process_value.connect(parent.set_progress_bar_value)
        self.signals.signal_process_max_range.connect(parent.set_process_max_range)
        self.signals.signal_status.connect(parent.print_status_to_label)

    def run(self) -> None:
        self.log.info('Main thread started.')
        self.all_files = get_all_filepath(self.subtitle_path)

        output_file_path = f'./result_{get_current_milli_time()}'

        if not self.all_files:
            self.signals.signal_no_subtitle_files.emit()
        else:
            self.signals.signal_process_max_range.emit(len(self.all_files))

            for idx, file in enumerate(self.all_files):
                self.log.info(f'Processing {file}')
                self.signals.signal_status.emit(f'Processing({idx + 1}-{len(self.all_files)}): {file}')

                result = convert(
                    input_file=file,
                    convert_to=self.convert_to,
                    output_file_path=output_file_path,
                    is_ori_encoding=self.is_ori_encoding,
                    is_ignore=self.is_ignore,
                    specified_encoding=self.encoding,
                    ass_headers=self.custom_ass_info,
                    convert_chinese_method=self.convert_chinese,
                    shift=self.offset
                )
                if not result.get('result'):
                    self.signals.signal_status.emit(result.get('msg'))

                self.signals.signal_process_value.emit(idx + 1)

        self.log.info('Main thread finished.')
        self.finished.emit()
