import time
import multiprocessing


def squared(numbers):
    print('Squared numbers')
    for n in numbers:
        time.sleep(0.2)
        print(f'{n}² = {n*n}')


def cube(numbers):
    print('Cubes numbers')
    for n in numbers:
        time.sleep(0.2)
        print(f'{n}³ = {n*n*n}')

numbers = [2, 3, 4, 5]

t0 = time.time()
thread_1 = multiprocessing.Process(target=squared, args=(numbers,))
thread_2 = multiprocessing.Process(target=cube, args=(numbers,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f'It took {time.time() - t0}s.')
