def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print "You have %d cheeses!" % cheese_count
    #print "You have %d boxes of crackers!" % boxes_of_crackers
    print(cheese_count, boxes_of_crackers)
    
    print "Man! thats enough for a party"
    print "Get a blanket.\n"

print "We can just give the function numbers directly"
cheese_and_crackers(20, 30)

print "Or we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 40

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do maths inside too:"
cheese_and_crackers(10 + 20, 15 + 35)

print "We can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

print "We can combine the two, variables and math:"
cheese_and_crackers(int(a) = 10, int(b) = 20)#-->wrong

def student(firstname, lastname): 
	print(firstname, lastname) 
	
	
# Keyword arguments				 
student(firstname =11, lastname =11)	 
student(lastname ='Practice', firstname ='Geeks') 


