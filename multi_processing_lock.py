import multiprocessing


# without locking critical section of code more than one process can access that section
# of code and produce undesired, unexpected results. Restrict access to only single process
# one at a time to ensure accuracy of program
def increment_sum(value, p_lock):
    for i in range(1000):
        p_lock.acquire()
        value.value += 1  # critical section
        p_lock.release()


def decrement_sum(value, p_lock):
    for i in range(1000):
        p_lock.acquire()
        value.value -= 1  # critical section
        p_lock.release()


if __name__ == '__main__':
    initial_sum = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()
    process_increment = multiprocessing.Process(target=increment_sum, args=(initial_sum, lock))
    process_decrement = multiprocessing.Process(target=decrement_sum, args=(initial_sum, lock))

    process_increment.start()
    process_decrement.start()

    process_increment.join()  # wait for process_increment to complete
    process_decrement.join()  # wait for process_decrement to complete

    print(initial_sum.value)
