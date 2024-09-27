import multiprocessing
import time


def true_waiter(cond):
    while True:
        with cond:
            print(multiprocessing.current_process().name)
            cond.wait()
            print('something happened')

def unlock_condition(cond):
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f'u must WAAIT! {i}')
        time.sleep(0.25)

if __name__ == '__main__':
    # multiprocessing.freeze_support()

    # Condition - выполняется еддиножды и дальше нам необходимо снова
    # вызвать notify, Event выполняется до того момента, пока стоит True
    cond = multiprocessing.Condition()
    pr = multiprocessing.Process(target=true_waiter, args=(cond,), daemon=False).start()
    pr2 = multiprocessing.Process(target=unlock_condition, args=(cond,), daemon=False).start()