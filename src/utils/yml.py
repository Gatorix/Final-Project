import logging.config

import yaml

from src.utils.files import resource_path, get_parent_path


class Yml:
    def __init__(self, file_path=None):
        if not file_path:
            self.file_path = resource_path(fr'{get_parent_path()}/config/saved_config.yml')
        else:
            self.file_path = file_path
        self.data = self.__load_yml()

    def __load_yml(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    def get_all_title(self):
        try:
            return list(self.data.keys())
        except AttributeError:
            return []

    def get_specific_details(self, title: str):
        try:
            return self.data.get(title)
        except AttributeError:
            return ''

    def write_info_to_yml(self, title, details):
        if title in self.get_all_title():
            return {'result': False, 'msg': 'Title cannot repeat.'}
        try:
            with open(self.file_path, 'a', encoding='utf-8') as file:
                yaml.dump({title: details}, file, default_style='>')
            return {'result': True, 'msg': 'Save Successful'}
        except Exception as e:
            return {'result': False, 'msg': e}

    def remove_specific_title(self, title):
        if title in self.get_all_title():
            self.data.pop(title)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            if len(self.get_all_title()) != 0:
                yaml.dump(self.data if self.data else None, file, default_style='>')
            else:
                file.truncate(0)


def logger():
    with open(resource_path(fr"{get_parent_path()}/config/logging.yml"), "r") as f:
        dict_conf = yaml.safe_load(f)

    logging.config.dictConfig(dict_conf)
    return logging.getLogger()
