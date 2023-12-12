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
    output_file = None

    if not os.path.isdir(output_file_path):
        os.mkdir(output_file_path)

    subs = pysubs2.load(input_file, encoding=input_file_encoding)

    if shift:
        subs.shift(s=shift)

    if 'txt' in convert_to:
        try:
            with open(
                    fr'{output_file_path}/{os.path.basename(input_file)}_Plain_Text.txt',
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
            encoding=input_file_encoding,
            format_='ass'
        )

        if ass_headers:
            change_ass_headers(output_file, ass_headers)

    elif 'srt' in convert_to:
        output_file = f'{output_file_path}/{Path(input_file).stem}.srt'
        subs.save(
            path=output_file,
            encoding=input_file_encoding,
            format_='srt'
        )
    else:
        return

    if convert_chinese_method:
        import opencc
        converter = opencc.OpenCC(convert_chinese_method)
        print(output_file)
        # with open(output_file, 'r', encoding=input_file_encoding) as f:
        #     converter.convert(f.read())


def change_ass_headers(file, headers):
    pass

if __name__ == '__main__':
# a= ass2srt(
#     r'C:\Users\kingdee\Desktop\Final-Project\test\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX.简体&英文.ass',
#     output_file_path='.',
#     specified_encoding='utf-8',
#     is_ignore=True,
#     convert_chinese_method='s2t'
# )
# print(a)
# srt2ass(r'C:\Users\kingdee\Desktop\Final-Project\test\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX.简体&英文.srt')
    fp = r'C:\Users\kingdee\Desktop\Final-Project\test\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX\Killers.Of.The.Flower.Moon.2023.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX.简体&英文.srt'
# input_file_encoding = get_file_encoding(fp)
#
# srt_subs = pysubs2.load(fp, encoding=input_file_encoding)
# srt_subs.shift(s=2.5)
# for line in srt_subs:
#     print(line.text)
#
# srt_subs.save('./test1.srt', input_file_encoding, format_='srt')

    convert(fp,'srt',convert_chinese_method='s2t')