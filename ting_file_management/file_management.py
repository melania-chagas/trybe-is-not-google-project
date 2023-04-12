import os
import sys


def check_file_format(path_file):
    # https://www.delftstack.com/pt/howto/python/python-get-file-extension/

    # os.path.splitext(file_path) retorna:
    # ('statics/arquivo_teste', '.txt')
    extension = os.path.splitext(path_file)
    return extension[1]


def txt_importer(path_file):
    extension = check_file_format(path_file)
    if extension != '.txt':
        return sys.stderr.write('Formato inválido')
    try:
        with open(path_file, 'r') as file:
            txt_file = file.read()
            return txt_file.split('\n')
    except IOError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')


# print(txt_importer('statics/arquivo_teste.txt'))
