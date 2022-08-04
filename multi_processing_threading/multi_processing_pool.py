# multi_processing_pool
# map_reduce usage

import multiprocessing


# each square_int operation is divided into multiple processes to expedite the computation
# i-e mapped to multiple processes and collected (reduced) from all processes after every
# process is done

def square_int(int_list):
    squared_list = list()
    for item in int_list:
        squared_list.append(item * item)
    print(str(squared_list))


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(square_int, (range(100),))
