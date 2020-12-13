from sys import argv

script, file_name = argv

print "We are going to erase %r." % file_name
print "If you dont want that hit ctrl-C (^C)."
print "If you do not want that hit RETURN."

raw_input("?")

print "Opening the file......."
target1 = open(file_name)
#target1 = open(file_name, mode='r', buffering=-1)

print target1.readline(5)
#print target1.readlines() -> works here

#print target1.read()

#print "Reading a line from the file.."
#print target1.readline(5) #not printing anything

#print "Reading multiple lines from the file.."
#print list(target1.readlines()) #only printing out []

print "closing the file"
target1.close()