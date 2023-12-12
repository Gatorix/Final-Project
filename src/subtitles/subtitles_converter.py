import os
from pathlib import Path

import pysubs2

from src.utils.files import get_file_encoding
from src.utils.times import get_current_milli_time


def convert(
        input_file,
        convert_to,
        is_ori_encoding=False,
        is_ignore=False,
        specified_encoding=None,
        ass_headers=None,
        convert_chinese_method=None,
        shift=0.0
):
    input_file_encoding = get_file_encoding(input_file)
    output_file_path = f'./result_{get_current_milli_time()}'

    if input_file.split('.')[-1] in convert_to:
        return {'result': False, 'msg': 'No conversion required.'}

    if not os.path.isdir(output_file_path):
        os.mkdir(output_file_path)

    subs = pysubs2.load(input_file, encoding=input_file_encoding)

    if shift:
        subs.shift(s=shift)

    if 'txt' in convert_to:
        try:
            output_file = fr'{output_file_path}/{os.path.basename(input_file)}_Plain_Text.txt'
            with open(
                    output_file,
                    'a',
                    encoding=input_file_encoding if is_ori_encoding else specified_encoding,
                    errors='ignore' if is_ignore else None
            ) as f:
                for line in subs:
                    f.write(f'{line.text}\n')
                return {'result': True, 'msg': 'Extract successful.'}
        except UnicodeEncodeError as uee:
            return {'result': False, 'msg': uee}

    elif 'ass' in convert_to:
        output_file = f'{output_file_path}/{Path(input_file).stem}.ass'
        subs.save(
            path=output_file,
            encoding=input_file_encoding if is_ori_encoding else specified_encoding,
            format_='ass'
        )

        if ass_headers:
            change_ass_headers(output_file, ass_headers)

    elif 'srt' in convert_to:
        output_file = f'{output_file_path}/{Path(input_file).stem}.srt'
        subs.save(
            path=output_file,
            encoding=input_file_encoding if is_ori_encoding else specified_encoding,
            format_='srt'
        )
    else:
        return {'result': False, 'msg': 'Unknown subtitle file.'}

    if convert_chinese_method:
        convert_chinese_of_file(output_file, convert_chinese_method)


def change_ass_headers(file, headers):
    pass


def convert_chinese_of_file(fp, cc_config):
    import opencc
    converter = opencc.OpenCC(cc_config)

    input_file_encoding = get_file_encoding(fp)

    with open(fp, 'r', encoding=input_file_encoding) as in_f:
        in_f_lines = in_f.readlines()
    with open(fp, 'w', encoding=input_file_encoding) as out_f:
        for _ in in_f_lines:
            out_f.write(converter.convert(_))


if __name__ == '__main__':
    fp1 = r'Z:\Users\caosheng\Documents\Code\Final-Project\test\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX\.简体&英文.srt'
    input_file_encoding1 = get_file_encoding(fp1)

    r=convert(fp1, 'ass', convert_chinese_method='s2t')
    print(r)
