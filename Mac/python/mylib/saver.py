from os import mkdir as os_mkdir
from os.path import exists as os_path_exists


def saver(path, content=True, txt=False):
    dir_path = ''.join(path.split('/')[:-1])

    os_mkdir(dir_path) if not os_path_exists(dir_path) else True
    if content:
        with open(path, 'wb') as f:
            f.write(content)
    elif(txt):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(txt)
