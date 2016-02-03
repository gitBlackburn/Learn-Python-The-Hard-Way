# sets the values of the people, cars and buses variables
people = 35
cars = 45
buses = 20

# compares cars to people and runs the code if the condition is met if the condition is not met it will run the code on the next line 
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take buses."
else:
	print "Fine, let's tay home then."
	
# additional practice example	
if people < buses and people == 35:
	print "BOY!HOWDY!"
else:
	print "Sup, dog?!"