import threading
import time

data = threading.local()

def get_data():
    print(data.name)

def thr1():
    data.name = 't1'
    get_data()

def thr2():
    data.name = '52'
    get_data()

t1 = threading.Thread(target=thr1, name='thr1')
t2 = threading.Thread(target=thr2, name='thr2')
t1.start()
t2.start()

def test():
    print(f'{threading.current_thread().name}')
    time.sleep(1)

t3 = threading.Timer(5, test)
t3.setName('threeeeeeead')
t3.start()

t4 = threading.Timer(100, test)
t4.setDaemon(True)
t4.start()

for i in range(4):
    print(f'something {i}')
    time.sleep(1)

t3.cancel()
print(f'canceled {t3.name}')

