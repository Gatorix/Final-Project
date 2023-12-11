import os
import sys

from charset_normalizer import detect


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def get_parent_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def get_current_path():
    return os.path.dirname(__file__)


def get_all_filepath(folder):
    # 获取指定路径下的所有*.ass, *.srt, *.vtt文件
    file_path = []
    for fpath, dirs, fs in os.walk(folder):
        for f in fs:
            if f.split('.')[-1] in ['srt', 'ass', 'vtt']:
                file_path.append(os.path.join(fpath, f))
    return file_path


def get_file_encoding(file):
    with open(file, 'rb') as f:
        return detect(f.read())['encoding']

# if __name__ == '__main__':
#     p = get_all_filepath(
#         r'C:\Users\kingdee\Desktop\Final-Project\test\S02')
#     print(p)
#     print(len(p))
#     t=r'C:\\Users\\kingdee\\Desktop\\Final-Project\\test\\Killers'
#     print(t.split('.')[-1])
