import multiprocessing
import time

def test(l):
    l.acquire()
    print(f'процесс {multiprocessing.current_process().name} - запущен')
    time.sleep(3)
    l.release()
    print(f'процесс {multiprocessing.current_process().name} - завершён')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    lock = multiprocessing.Lock()
    multiprocessing.Process(target=test, args=(lock,), name='procces-1').start()
    multiprocessing.Process(target=test, args=(lock,), name='procces-2').start()