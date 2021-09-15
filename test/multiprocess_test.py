# Multiprocessing test

# https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing

# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == "__main__":
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))


### ---------------------------------------------------------

# from multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('Module name:', __name__)
#     print('PPID:', os.getppid())
#     print('PID:', os.getpid())

# def f(name):
#     info('Function f')
#     print("Hey, this is", name)

# if __name__ == "__main__":
#     info('Main line')
#     p = Process(target=f, args=('proc1',))
#     print("a")
#     p.start()
#     print("b")
#     p.join()
#     print("c")

### ---------------------------------------------------------

import multiprocessing as mp

def enqueue(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=enqueue, args=(q,))
    p.start()
    print(q.get())
    p.join()