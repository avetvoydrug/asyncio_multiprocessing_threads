import multiprocessing
import time
from random import randint

class Tester:
    upgraded = []

    def __init__(self, value):
        self.name = f'obj: {value}'
        self.value = value

    def __str__(self) -> str:
        return f'{self.name}: {self.value}'

    @staticmethod
    def printer(response):
        print('all_right')
        a = [str(i) for i in response]
        print(a)

    @staticmethod
    def test_pool(obj):
        obj.upgraded.append(obj)
        s = randint(-214,214)
        obj.value += s
        print(f'name: {multiprocessing.current_process().name}, значение: {obj.value} name_obj: {obj.name}\n')
        return obj

if __name__ == '__main__':
    need_upgrade = [Tester(i) for i in range(200)]
    if need_upgrade:
        time.sleep(2)
        # Pool принимает кол-во процессов и запускает их всех
        # как только процесс завершает свою  работу, если элементы итератора не закончились
        # то процесс снова попадает в Pool и выполняет свои действия
        # использовать, например, при парсинге страниц
        with multiprocessing.Pool(multiprocessing.cpu_count() * 2) as p:
            # map args - метод, итератор
            # p.map(Tester.test_pool, need_upgrade)

            # map_async - позволяет после завершения всех процессов
            # запустить необходимый call_back - со списком результатов всех процессов
            p.map_async(Tester.test_pool, need_upgrade, callback=Tester.printer)
            # при использовании map_async необходимо закрыть Pool и join()
            p.close()
            p.join()

            # apply_asinc принимает аргументы и после завершения каждого процесса
            # вызывает callback с результатом отработки процесса
            # p.apply_async(target, args=(x,), callback=end_func)

            # starmap принимает target, итератор из кортежей аргументов и callback
            # callback вызывается после отработки всех процессов с их резльтатами