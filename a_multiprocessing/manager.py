import multiprocessing

# Manager позволяет использовать общую память, создавать структуры
# и передавать их между процессами

def change_srtuct(m_array, m_dict):
    m_array.append(f'appended from {multiprocessing.current_process().name}')
    m_dict['appended'] = f'from {multiprocessing.current_process().name} '

if __name__ == '__main__':
    with multiprocessing.Manager() as m:
        lis = m.list()
        dic = m.dict()
        pr = multiprocessing.Process(target=change_srtuct, args=(lis, dic))
        pr.start()
        pr.join()
        print(lis, dic, multiprocessing.current_process().name)