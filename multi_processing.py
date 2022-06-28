import multiprocessing
import time


def some_cpu_intensive_work(init_range):
    sum = 0
    for i in range(init_range):
        sum += i
    print(sum)


def some_other_cpu_intensive_work(init_range):
    squared_sum = 0
    for i in range(init_range):
        squared_sum += i * i
    print(squared_sum)


# Windows lacks os.fork() it has a few extra restrictions:
# https://docs.python.org/2/library/multiprocessing.html#windows
if __name__ == '__main__':
    # Multiprocessing (utilising cpu cores) is useful where we have computational work

    start_time_multiprocessing = time.time()
    process_1 = multiprocessing.Process(target=some_cpu_intensive_work, args=(100000000,))
    process_2 = multiprocessing.Process(target=some_other_cpu_intensive_work, args=(100000000,))

    process_1.start()
    process_2.start()

    process_1.join()  # wait for process_1 to complete
    process_2.join()  # wait for process_2 to complete

    print(f"time taken with multiprocessing: {time.time() - start_time_multiprocessing}")

    start_time_without_multiprocessing = time.time()
    some_cpu_intensive_work(100000000)
    some_other_cpu_intensive_work(100000000)
    print(f"time taken without multiprocessing: {time.time() - start_time_without_multiprocessing}")
