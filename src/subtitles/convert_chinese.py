import opencc


def convert_chinese(text, config):
    converter = opencc.OpenCC(config)
    return converter.convert(text)
