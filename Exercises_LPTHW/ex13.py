from sys import argv
#command line args comes as in string, so if we want an int value we have to use int()

script, first, second, third = argv
#script, int(first), int(second), third = argv --> cant do like int(first) 
n1 = int(first)
n2 = int(second)

print "The scriptis called:", script
print "Your first variable is:", first
#print "Your first variable is:", int(first)
print "Your second variable is:", second
print "Your third variable is:", third
print "Addition of 1st and 2nd variable is:", n1 + n2

n3 = int(raw_input("enter anumber:"))
print "Addition of 1st and last variable is:", n1 + n3


#output: if i give only one argument in the command line ie.- ex13.py
#PS C:\Users\Manisha\mystuff> python ex13.py
#Traceback (most recent call last):
#  File "ex13.py", line 3, in <module>
#    script, first, second, third = argv
#ValueError: need more than 1 value to unpack