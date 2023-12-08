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
    # 获取指定路径下的所有.ass文件
    file_path = []
    for fpath, dirs, fs in os.walk(folder):
        for f in fs:
            if '.DS_Store' in os.path.join(fpath, f):
                pass
            elif os.path.join(fpath, f)[-4:] != '.ass':
                pass
            else:
                file_path.append(os.path.join(fpath, f))
    return file_path


def get_file_encoding(file):
    with open(file, 'rb') as f:
        return detect(f.read())['encoding']
