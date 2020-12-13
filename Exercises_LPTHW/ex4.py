cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
avg_passengers_per_car = passengers / cars_driven
#avg_passengers_per_car = carpool_capacity / passengers 
#Traceback (most recent call last):
  #File "ex4.py", line 9, in <module>
    #avg_passengers_per_car = carpool_capacity / passengers
#NameError: name 'carpool_capacity' is not defined -->> will get this error if we comment out line#7

print "There are", cars, "cars driven"
print "There are only", drivers, "drivers available"
print "There will be", car_not_driven, "empty cars"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to car pool today"
print "We need to put about", avg_passengers_per_car, "in each car"
#print "We %s are." % "done!"