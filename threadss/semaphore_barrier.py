from threading import Thread, BoundedSemaphore, Barrier, current_thread
import time
from random import randint


max_threads = 5
pool = BoundedSemaphore(value=max_threads)
# Semaphore принимает макс число потоков, добавляет следующий, как только какой-нибудь
# поток завершил своё выполнение

def something_with_semaphore():
    with pool:
        print(current_thread().name)
        time.sleep(4)              


for i in range(10):
    Thread(target=something_with_semaphore, name=f'thr-{i}')
# барьер также  принимает макс кол-во потоков, но ждёт, пока каждый вызовет метод wait()
# и только потом разблокирует места для других, т.е. выкидывает своеобразными пачками
#Barrier() - не поддерживает with
# можно использовать при отправке данных - допустим, пока все потоки не подгрузят необх. данные
# и не вызовут метод wait(), отправкане произойдёт

bar = Barrier(parties=max_threads)
def somethind_with_barrier(barrier):
    slp = randint(2,5)
    time.sleep(slp)
    print(f'{current_thread().name} - started at: {time.ctime()} | sleeping: {slp}')
    barrier.wait()
    print(f'{current_thread().name} - ended at: {time.ctime()}')

for i in range(5):
    # target - метод; args - передаваемые аргументы(кортеж,)
    Thread(target=somethind_with_barrier, args=(bar,), name=f'thr-{i}').start()
