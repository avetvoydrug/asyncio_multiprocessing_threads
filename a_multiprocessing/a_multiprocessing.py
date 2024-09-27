import multiprocessing
import time


# Принцип создания процессов тот же, что и у потоков
# чтобы запустить процесс из класса нужно переопределить метод run()
# т.к. он вызывает target, а target мы не передаём явно

class Proc(multiprocessing.Process):

    def run(self):
        print(f'шатаут братка!')


def test():
    i = 0
    while True:
        print(f'{multiprocessing.current_process().name}')
        time.sleep(1)
        i += 1
        if i == 5:
            multiprocessing.current_process().terminate()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    some_p = Proc()
    some_p.start()
#     time.sleep(5)
#     p = multiprocessing.Process(target=test, name='process')
#     p.start()
#     print(f'процесс {p.name} запущен')
#     p.join()
#     print(f'процесс {p.name} завершл работу')
#     time.sleep(10)