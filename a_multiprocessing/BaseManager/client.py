from multiprocessing.managers import BaseManager


# BaseManager.register('get')
mng = BaseManager(address=('127.0.0.1', 4444),  authkey=b'abc')
mng.register('get')
mng.connect()

res = mng.get()
print(res)