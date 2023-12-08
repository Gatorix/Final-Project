import os
from pathlib import Path

from pysubparser import parser

from src.utils.files import get_file_encoding
from src.utils.times import get_current_milli_time


def extract_plain_text(
        input_file,
        output_file_path='.',
        output_file_encoding='utf-8',
        is_ignore=None
):
    input_file_encoding = get_file_encoding(input_file)
    subtitles = parser.parse(input_file, encoding=input_file_encoding)

    if not os.path.isdir(output_file_path):
        os.mkdir(output_file_path)

    try:
        with open(
                fr'{output_file_path}/{Path(input_file).stem}_Plain_Text_{get_current_milli_time()}.txt',
                'a',
                encoding=output_file_encoding,
                errors='ignore' if is_ignore else None
        ) as f:
            for subtitle in subtitles:
                f.write(f'{subtitle.text}\n')
            return {'result': True, 'msg': 'Extract successful.'}
    except UnicodeEncodeError as uee:
        return {'result': False, 'msg': uee}
