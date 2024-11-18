import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self,name,power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        count_day = 0
        count_warriors = 100
        print(f'{self.name}, на нас напали!')
        while count_warriors:
            sleep(1)
            count_warriors -= self.power
            count_day += 1
            print(f'{self.name} сражается {count_day} день, осталось {count_warriors} воинов')
        print(f'{self.name} одержал победу спустя {count_day} дней')


first_knight = Knight('Sir Lancelot',10)
second_knight = Knight('Sir Galahad',20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')