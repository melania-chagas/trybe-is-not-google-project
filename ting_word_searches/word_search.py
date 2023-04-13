from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def get_occurrences(word, file_lines):
    occurrences = []
    for i, line in enumerate(file_lines):
        if word.lower() in line.lower():
            occurrences.append({
                'linha': i + 1
            })
    return occurrences


def exists_word(word, instance):
    instance_list = list(instance.queue)
    file_lines = instance_list[0]['linhas_do_arquivo']

    if get_occurrences(word, file_lines) == []:
        return []

    return [{
        'palavra': word,
        'arquivo': instance_list[0]['nome_do_arquivo'],
        'ocorrencias': get_occurrences(word, file_lines)
    }]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


queue = Queue()
process('statics/arquivo_teste.txt', queue)
print(exists_word('de', queue))
