from sys import argv

script, file_name = argv

print "We are going to erase %r." % file_name
print "If you dont want that hit ctrl-C (^C)."
print "If you do not want that hit RETURN."

raw_input("?")

print "Opening the file......."
#Open the file in write mode, if filename entered is not there it will 
#create a new file and if file already exist, it will erase the content 
#and write with new content.
target = open(file_name, 'w') 

print "Trancating the file. Goodbye!!"

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I am going to write these to the file."

#write the lines-line1, line2 and line3 into the file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#Theres too much repetition in this file. Use strings, formats, and escapes to print out
#line1, line2, and line3 with just one target.write() command instead of six.
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
#target.write('{}\n{}\n{}\n'.format(line1, line2, line3))

print "And finally we close it."
target.close()

print "Reading the file.."
target1 = open(file_name)
#target1 = open(file_name, mode='r', buffering=-1)
print target1.read()

#print "Reading a line from the file.."
#print target1.readline()

#print "Reading multiple lines from the file.."
#print target1.readlines()

print "closing the file"
target1.close()


