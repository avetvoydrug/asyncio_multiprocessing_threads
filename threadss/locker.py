import threading
import time

value = 0

locker = threading.Lock()

def add_one():
    global value
    while value < 100:
        # with locker:
        locker.acquire()
        value += 1
        print(value, threading.current_thread().name)
        time.sleep(0.01)
        locker.release()
        #if value % 5 == 0:
        # - плохая практика оба потока блокируются - приводит к ошибке
        #    locker.release()


t1 = threading.Thread(target= add_one, name='first')
t2 = threading.Thread(target= add_one, name='second')
t1.start()
t2.start()