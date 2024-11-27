from queue import Queue
import threading
from time import sleep
import random


class Table:
    def __init__(self,number,guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.uniform(3,10))


class Cafe:
    def __init__(self,*tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self,*guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}.')
                    table.guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        while not self.queue.empty() or sum([0 if table.guest is None else 1 for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()