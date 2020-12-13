from sys import argv

script, file_name = argv

#open the file and returns a stream
txt = open(file_name)


print "Here is your file %r." % file_name
print txt.read()

#print "Type the file name again"
#file_again = raw_input("> ")

#txt_again = open(file_again)
#print txt_again.read()

txt1 = open("ex15_sample1.txt", "a")

txt1.write("Hello world!!")
txt1.close()
txt.close()
