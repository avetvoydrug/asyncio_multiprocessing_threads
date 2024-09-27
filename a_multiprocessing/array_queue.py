import multiprocessing
from random import randint

# Array, queue - позволяет использовать синхронизированные данные в разных процессах

def test_array(l, arr, index):
    with l:
        num = randint(15,500)
        arr[index] = num
        print(f'{multiprocessing.current_process().name} arr[{index}] - {num}')

def test_queue(l, q):
    with l:
        num = randint(754,9459)
        q.put(num)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    arr = multiprocessing.Array('i', range(10))
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    process = []
    for i in range(10):
        # pr = multiprocessing.Process(target=test_array, args=(lock, arr, i),  name=f'process-{i}')
        pr = multiprocessing.Process(target=test_queue, args=(lock, queue),  name=f'process-{i}')
        # daem = randint(0,1)
        # pr.daemon = daem
        # print(i, daem)
        pr.start()
        process.append(pr)
    
    for i in process:
        i.join()

    for i in iter(queue.get, None):
        print(i)
    #print(list(arr))