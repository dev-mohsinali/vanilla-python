def decorate_greeting_with_custom_message(func):
    def inner():
        print ('started executing',func.__name__)
        func()
        print ('finished executing',func.__name__)
    return inner
    
@decorate_greeting_with_custom_message
def print_greeting():
    print("hello there")

print_greeting()