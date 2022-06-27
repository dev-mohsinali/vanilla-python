import threading
import time


# Threads are usable where we have IO bound tasks
# For computational work use multiprocessing

def some_io_work(init_range):
    sum = 0
    for i in range(init_range):
        time.sleep(0.1)
        sum += i
    print(sum)


def some_other_io_work(init_range):
    squared_sum = 0
    for i in range(init_range):
        time.sleep(0.1)
        squared_sum += i * i
    print(squared_sum)


start_time_threading = time.time()
task_1 = threading.Thread(target=some_io_work, args=(5,))
task_2 = threading.Thread(target=some_other_io_work, args=(4,))

task_1.start()
task_2.start()

task_1.join()  # wait for task_1 to complete
task_2.join()  # wait for task_2 to complete

print(f"time taken with threading: {time.time() - start_time_threading}")

start_time_without_threading = time.time()
some_io_work(5)
some_other_io_work(4)
print(f"time taken without threading: {time.time() - start_time_without_threading}")
