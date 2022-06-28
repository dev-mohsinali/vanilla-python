import multiprocessing
import time

result = []


def some_cpu_intensive_work(init_range, shared):
    global result
    sum = 0
    for i in range(init_range):
        sum += i
    shared.value = sum
    result.append(sum)
    print(f" result of sum within process is: {str(result)}")


# Windows lacks os.fork() it has a few extra restrictions:
# https://docs.python.org/2/library/multiprocessing.html#windows
if __name__ == '__main__':
    # creating shared memory
    shared_result = multiprocessing.Value('d', 0.0)
    # Multiprocessing (utilising cpu cores) is useful where we have computational work
    process_1 = multiprocessing.Process(target=some_cpu_intensive_work, args=(100000000, shared_result))
    process_1.start()
    process_1.join()  # wait for process_1 to complete

    # won't work as child process can not access memory of main process
    print(f" result of sum outside main process is: {str(result)}")

    print(shared_result.value)  # shared memory address between main and child process

    # child process crates copies of main process variables but does not directly link to address
    # space of main process unlike threads where there is single process and memory is shared among
    # threads as they have access to same process memory
