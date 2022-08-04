def print_msg(message):
    greeting = "Hello"
    def printer():
        print(greeting,message)
    return printer

# print_msg is done executing at this line
func = print_msg("python is great")

# when we append () with func printer method is returned/called
# printer remembers the value of greeting and message
# printer function defined as inner function is closure here
# closure is any function which remembers its scope level values even if 
#outer function is done executing

func() #calling printer()