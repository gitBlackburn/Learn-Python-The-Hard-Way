# We have one hundreded cars 
cars = 100
# There is enough room for four people in each car
space_in_car = 4
# There are thirty drivers
drivers = 30
# There are nintey passengers 
passengers = 90
# The number of cars not driven is equal to the total number of cars minus the number of drivers
cars_not_driven = cars - drivers
# The number of cars driven is equal to the number of drivers
cars_driven = drivers
# The carcapcity is equal to the product of the cars driven and the space in a car
carpool_capcity = cars_driven * space_in_car
# The average number of passangers in a car is equal to the number of pasengers divided by the cars driven
average_passengers_per_car = passengers / cars_driven

print 'There are ', cars, 'cars available.'
print 'There are only', drivers, 'drivers avaiable.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capcity, 'people today.'
print 'We have ', passengers, ' to carpool today.'
print 'We need to put about', average_passengers_per_car, 'in each car.'