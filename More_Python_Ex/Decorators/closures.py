
def outer_func(msg):

    def inner_func():
        print(msg)
    
    return inner_func


hi_func = outer_func('hi')
# print(hi_func.__name__)
hi_func()

hello_func = outer_func('hello')
# print(hello_func.__name__)
hello_func()