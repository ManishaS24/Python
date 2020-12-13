# # some practical examples

def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

    def wrapper_func(*args, **kwargs):
        logging.info(
            'ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return original_func(*args, **kwargs)
    
    return wrapper_func



def my_timing(original_func):
    import time
    
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        
        print('{} ran in: {} sec'.format(original_func.__name__, t2))
        return result
    
    return wrapper_func

# @my_logger
# def display_info(name, age):
#     print('display info ran with arguments ({}, {})'.format(name, age))

# display_info('John', 30)

import time

@my_timing
def display_info(name, age):
    time.sleep(1)
    print('display info ran with arguments ({}, {})'.format(name, age))

display_info('Ron', 30)
