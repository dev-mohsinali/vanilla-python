class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):  # called as soon as it enters with block
        print("__enter__ called")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # called when exited with block
        if self.file:
            self.file.close()
        print("__exit__ called")
        # return True  #if True is returned from exit exception raised here is ignored


with ManagedFile("../myfile.txt") as file:
    file.write("some text")
