from urllib import request as r
import math
import os


def nice(size_bytes):
    if size_bytes == 0:
        return "0B"
    units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    converted_size = round(size_bytes / p, 2)
    return f'{converted_size} {units[i]}'


def save_file(url, name=None, path=None):
    if not name:
        name = url.split('/')[-1]
    if not path:
        path = name
    file_to_download = r.urlopen(url)
    file = open(path + '.download', 'wb')
    file_size = file_to_download.length
    nice_size = nice(file_size)
    print(f'Downloading {nice_size} {name}:')

    downloaded = 0
    block_size = 8192
    buffer = 1

    while buffer:
        buffer = file_to_download.read(block_size)
        downloaded += len(buffer)
        file.write(buffer)
        progress_percents = downloaded * 100 // file_size
        progress_bar = progress_percents//5
        print(f'\r{"#" * progress_bar}{"-" * (20-progress_bar)} {progress_percents}% '
              f'{nice(downloaded)} / {nice_size}', end='')

    file.close()
    if path in os.listdir():
        os.remove(path)
    os.rename(path + '.download', name)
