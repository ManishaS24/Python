#this is more like the script with argv
def print_two(*args):
    arg1, arg2 = args #unpacking of args
    print "arg1: %r \narg2: %r" % (arg1, arg2)

#ok that *args is pointless. We can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg):
    print "arg: %r." % arg

# this one takes no arguments
def print_none():
    print "Prints nothing"

print_two("Manisha", "Sinha")
print_two_again("Minu", "Sinha")
print_one("Mitu")
print_none()