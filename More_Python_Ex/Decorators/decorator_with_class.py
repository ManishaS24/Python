class decorator_class(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('call function executed before "{}"'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)
    
    

@decorator_class #same as line 15
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    print('display info ran with arguments ({}, {})'.format(name, age))

display_info('John', 30)
display()