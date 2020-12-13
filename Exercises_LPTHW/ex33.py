i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i

print "The numbers:"
for n in numbers:
   print n

def num_func(stop, step):
    j = 0
    while j < stop:
        print "At the top j is %d" % j
        numbers.append(j)
        j = j + step
        print "numbers now:", numbers
        print "At the bottom j is %d" % j

    print numbers   

num_func(10,2)    

del numbers[0:11]
print numbers

def num_func_again(stop, step):
    for i in range(0,stop,step):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
        print "numbers now:", numbers

num_func_again(10, 2)