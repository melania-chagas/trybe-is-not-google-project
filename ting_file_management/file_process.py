from ting_file_management.file_management import txt_importer
import sys
# from ting_file_management.queue import Queue


def process(path_file, instance):
    instance_list = list(instance.queue)
    for file in instance_list:
        if file['nome_do_arquivo'] == path_file:
            return None

    file_list = txt_importer(path_file)
    if len(file_list) >= 0:
        file_dict = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(file_list),
            'linhas_do_arquivo': file_list,
        }
        instance.enqueue(file_dict)
        return sys.stdout.write(str(file_dict))


def remove(instance):
    instance_list = list(instance.queue)
    if len(instance_list) == 0:
        return sys.stdout.write('Não há elementos\n')
    dequeue = instance.dequeue()
    path_file = dequeue['nome_do_arquivo']
    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# queue = Queue()
# process('statics/arquivo_teste.txt', queue)
# print(remove(queue))
