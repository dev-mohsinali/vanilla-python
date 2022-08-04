# decorator is any function that wraps around another passed function
# to enhance its functionality

#closure or inner function can return passed function or any value
#like here we are returning func call (not func itself) based on y's value 
# else string is returned

def math_divisonbyzero_decorator(func):
    def closure(x,y):
        if y==0:
            return 'undefined'
        return func(x,y)
    return closure
    
@math_divisonbyzero_decorator
def divide(x,y):
    return x/y


# using decorator attribute simplifies call
print(divide(10,2))

#without decorator attribute
print(math_divisonbyzero_decorator(divide)(10,2))

