 # - -coding: utf- 8 - 
my_name = "Manisha Sinha"
my_age = 26
my_height = 5 #feet
my_weight = 41 #kgs
my_eyes = "Brown"
my_teeth = "white"
my_hair = "Black"

print "Now lets talk about %s" % my_name
print "She's %d feet tall" % my_height
print "She's %d kgs heavy" % my_weight
print "Actually thats not too heavy"
print "She's got %s hair and %s eyes" % (my_hair, my_eyes)
print "Her teeth are %s usually depending on the coffee" % my_teeth

#this line is tricky try to get it right
print "If I add %d, %d and %d I get %d" % (
       my_age, my_height, my_weight, my_age + my_height + my_weight)
print "Hi %r manisha" % my_age #o/p:- Hi 26 --> it will ignore string after %r and print the rest 