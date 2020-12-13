print "You enter a dark room with two doors. Do you go with door #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "There's a gian bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    if bear == "1":
	    print " Good job!"
    elif bear == "2":
        print "Good job!"
    else:
	    print "Well, doing %s is probably better. Bear runs away!" % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print " Good job!"
    else:
        print "Good job!"

else:
    print "Good job!"

		