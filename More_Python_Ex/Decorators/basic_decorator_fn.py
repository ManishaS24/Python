# def decorator_func(original_func):

#     def wrapper_func():
#         print('wrapper executed before "{}"'.format(original_func.__name__))
#         return original_func()
    
#     return wrapper_func

# @decorator_func #same as line 20
# def display():
#     print('display function ran')

# @decorator_func
# def display_info(name, age):
#     print('display info ran with arguments ({}, {})'.format(name, age))

# display_info('Tom', 20)
# display()

# decorated_display = decorator_func(display)
# decorated_display()

def decorator_func(original_func):

    def wrapper_func(*args, **kwargs):
        print('wrapper executed before "{}"'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    
    return wrapper_func

@decorator_func 
def display():
    print('display function ran')

@decorator_func
def display_info(name, age):
    print('display info ran with arguments ({}, {})'.format(name, age))

display_info('John', 30)
display()