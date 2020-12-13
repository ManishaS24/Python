def prefix_decorator(prefix):
    def decorator_func(original_func):
        def wrapper_func(*args, **kwargs):
            print(prefix, "Executed before", original_func.__name__)
            result = original_func(*args, **kwargs)
            print(prefix, "Executed after", original_func.__name__)
            return result
        return wrapper_func
    return decorator_func

@prefix_decorator('LOG:')
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info('Rama', 25)
display_info('Radha', 30)