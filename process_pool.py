from multiprocessing import Pool
import os
import time

def tets_pool(msg):
    print('subprocess {} start'.format(msg))
    time.sleep(1)
    print('subprocess {} end'.format(msg))

if __name__ == '__main__':
    print('start main process')
    pool = Pool(processes=os.cpu_count())
    for i in range(1, 11):
        pool.apply_async(tets_pool, args=(i,))
    pool.close()
    pool.join()
    print('end main process')
