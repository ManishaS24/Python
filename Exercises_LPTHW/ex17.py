from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We could do these two in one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes ling" % len(indata)

print "Does the output file exist?%r." % exists(to_file)

print "Hit RETURN to continue and Ctrl-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright..All Done!"

#in_file.close()
out_file.close()
