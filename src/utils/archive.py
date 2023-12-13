import os
import shutil
import zipfile


def zip_fp(fp):
    if not os.path.isdir(fp):
        return
    file_news = f'{fp}.zip'
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, filenames in os.walk(fp):
        fpath = dir_path.replace(fp, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dir_path, filename), fpath + filename)

    z.close()

    shutil.rmtree(fp)
