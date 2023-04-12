from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    # https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/7939c08a-6df3-4e20-81f3-9581c68d940b/day/c55250a2-6d5d-4dba-a336-4e9a9a0cc6b5/lesson/3e8d2d24-12c8-42e7-8496-2dd535418949

    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        # Enqueue: Adiciona um elemento no final da fila
        self.queue.append(value)

    def dequeue(self):
        # Dequeue: Remove e retorna o primeiro elemento da fila
        if len(self.queue) == 0:
            # Se não houver mais itens na fila, o método retornará None
            return None
        # O método pop remove e retorna o valor do índice fornecido
        return self.queue.pop(0)

    def search(self, index):
        error_message = "Índice Inválido ou Inexistente"
        if index < 0 or index >= len(self.queue):
            raise IndexError(error_message)
        return self.queue[index]
