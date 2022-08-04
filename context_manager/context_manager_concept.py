# Allows to obtain and release resources without explicit calls for resource attainment/release
with open('../myfile.txt', 'w') as file:
    file.write("some text")

# without the context manager usage
try:
    file = open('../myfile.txt', 'w')
    file.write("some text")
finally:
    file.close()  # release file resource
