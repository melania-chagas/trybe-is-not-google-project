from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def get_occurrences(word, file_lines, keyword):
    occurrences = []

    for i, line in enumerate(file_lines):

        if word.lower() in line.lower():
            occurrence = {'linha': i + 1}

            if keyword == 'search_by_word':
                occurrence = {
                    'linha': i + 1,
                    'conteudo': line
                }

            occurrences.append(occurrence)

    return occurrences


def exists_word(word, instance, keyword=None):
    instance_list = list(instance.queue)
    file_lines = instance_list[0]['linhas_do_arquivo']

    if get_occurrences(word, file_lines, keyword) == []:
        return []

    return [{
        'palavra': word,
        'arquivo': instance_list[0]['nome_do_arquivo'],
        'ocorrencias': get_occurrences(word, file_lines, keyword)
    }]


def search_by_word(word, instance):
    keyword = 'search_by_word'
    return exists_word(word, instance, keyword)


queue = Queue()
process('statics/arquivo_teste.txt', queue)
print(search_by_word('de', queue))
