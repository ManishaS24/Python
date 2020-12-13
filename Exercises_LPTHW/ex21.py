def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def mult(a, b):
    print "MULTIPLICATION %d * %d" % (a, b)
    return a * b

def div(a, b):
    print "DIVISION %d / %d" % (a, b)
    return a / b

def mod(a, b):
    print "MODULO %d mod %d" % (a, b)
    return a % b

def inverse(a):
    print "INVERSE of %d" % a
    return 1.0 / a
	
print "Lets do some math with just functions"

age = add(20, 5)
height = subtract(166, 67)
weight = mult(7, 6)
iq = div(32, 4)
modulo = mod(10, 3)

print "Age: %d, Height: %d, Weight: %d, iq: %d, Modulo: %d" % (age, height, weight, iq, modulo)

#A puzzle for the extra credit, type it in anyway
print "Here is a puzzle.."

what = add(age, subtract(height, mult(weight, div(iq, 2))))

print "That becomes:", what, "can you do it by hand?"

print inverse(21)