from sys import exit

def check_temp():
    print "What is your temperature?"
    temp = raw_input("> ")
    if temp > 98:
        dead_room("You are infected..")
    else:
        print "You are allowed to enter last room"
        
    

def dead_room(why):
    print why, "^.^"
    exit(0)

def last_room():
    check_temp()
    print "YEY!! You WON!!"
    exit(0)

def dark_room():
    print "You are in the dark room, so be CAREFULL!!"
    print "Choose your way carefully.."
    print "Which way you want to go next??(left / right)"
    
    which_way = raw_input("> ")
    if which_way == "left":
        dead_room("You are in a room of infected poeple..OOPS!!")
    elif which_way == "right":
        last_room()
    else:
        exit(0)

def dim_room():
    exit(0)

def start():
    print "Welcome to this SKIP CORONA game!!"
    print "There is two doors, LEFT or RIGHT"
    print "Which one do you take??"
	
    which_way = raw_input("> ")
    
    if which_way == "left":
		dark_room()
    elif which_way == "right":
        dim_room()
    else:
        print "There is no such option.SORRY!!.."
        print "Do want to try this game again??(Y/N)"
		
        choice = raw_input("> ")
    if choice == "Y" or choice == "y":
        start()
    elif choice == "N" or choice == "n":
        print "Thank you for trying this game..:))"
        exit(0)
    else:
        exit(0)

start()