import time
import multiprocessing


def squared(numbers, result, v):
    print('Squared numbers')
    for i, n in enumerate(numbers):
        time.sleep(0.2)
        result[i] = n*n
    v.value = 3.41
    print(v.value)
    print(list(result))

numbers = [2, 3, 4, 5]
result = multiprocessing.Array('i', 4)
v = multiprocessing.Value('d', 0.0)

t0 = time.time()
thread_1 = multiprocessing.Process(target=squared, args=(numbers, result, v))

thread_1.start()
thread_1.join()

print(f'It took {time.time() - t0}s.')
