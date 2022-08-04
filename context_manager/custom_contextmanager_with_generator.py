from contextlib import contextmanager


@contextmanager
def managed_file(filename):
    try:
        file = open(filename, "w")
        yield file
    finally:
        file.close()


with managed_file("../myfile.txt") as my_file:
    my_file.write("some text")
