import threading
import time


def get_data(data):
    print(f'{threading.active_count()}\n')
    print(f'{threading.enumerate()}\n')
    a = 5
    if threading.current_thread().name == 'som_thread':
        a = 2

    for i in range(a):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)

thr = threading.Thread(target= get_data, name='som_thread', args=(str(time.time()),))
# target - ссылка на функцию | поток, 
# daemon - если True завершается вместе с основным потоком, False(by default) - работает в фоне
daemon_thr = threading.Thread(target= get_data, name='some_daemon_thread', 
                              args=(str(time.time()),), daemon=True)
thr.start()
daemon_thr.start()
#thr.join() # join блокирует дальнейшее выполнение кода


print('finish\n')