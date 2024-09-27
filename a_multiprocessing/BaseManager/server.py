from multiprocessing.managers import BaseManager
from multiprocessing import current_process
from time import ctime


def pool():
    return f'{current_process().name} connected at {ctime()}'

manager = BaseManager(address=('',  4444), authkey=b'abc')
manager.register('get', callable=pool)
print('Server now running')
manager.get_server().serve_forever()