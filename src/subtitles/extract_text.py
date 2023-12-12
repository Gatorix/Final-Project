﻿import os
import re

from pysubparser import parser

from src.subtitles.convert_chinese import convert_chinese
from src.utils.files import get_file_encoding


def extract_plain_text(
        input_file,
        output_file_path=None,
        is_ori_encoding=False,
        specified_encoding=None,
        is_ignore=False,
        convert_chinese_method=None
):
    input_file_encoding = get_file_encoding(input_file)
    subtitles = parser.parse(input_file, encoding=input_file_encoding)

    if not os.path.isdir(output_file_path):
        os.mkdir(output_file_path)

    try:
        with open(
                fr'{output_file_path}/{os.path.basename(input_file)}_Plain_Text.txt',
                'a',
                encoding=input_file_encoding if is_ori_encoding else specified_encoding,
                errors='ignore' if is_ignore else None
        ) as f:
            for subtitle in subtitles:
                if convert_chinese_method:
                    f.write(f'{convert_chinese(subtitle.text, convert_chinese_method)}\n')
                else:
                    f.write(f'{subtitle.text}\n')
            return {'result': True, 'msg': 'Extract successful.'}
    except UnicodeEncodeError as uee:
        return {'result': False, 'msg': uee}


def extract_text_between_bracket(text):
    pattern = r'\(.*?\)'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        return match[1:-1]
