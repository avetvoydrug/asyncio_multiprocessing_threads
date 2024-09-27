import multiprocessing
from time import sleep, ctime
from random import randint


def barrier(bar):
    slp = randint(1,5)
    print(f'{multiprocessing.current_process().name}, sleep: {slp}, started at {ctime()}\n')
    sleep(slp)
    bar.wait()
    print(f'{multiprocessing.current_process().name} finished\n')


if __name__ == '__main__':
    # Barrier(k) ждёт, пока выполняться любые первые k процессов
    # затем выплёвывает их и запускает следующие, если не наберётся
    # k процессов Barrier будет ожидать, пока не заполнится до конца
    bar = multiprocessing.Barrier(5)

    for i in range(10):
        multiprocessing.Process(target=barrier, args=(bar,), daemon=False).start()