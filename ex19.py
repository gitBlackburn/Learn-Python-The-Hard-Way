# creates a function called cheese and crackers that takes two 
# arguments and prints them with some strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# print statement	
print "We can just give the function numbers directly:"
# function call 
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# function call with variables 
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)



print "We can even do math inside too:"
# a functioncal that shows we can pass math equations as arguments
cheese_and_crackers(10 +20, 5+ 6)


print "And we can combine the two, variables and math:"
# third function call that uses integers and variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def kate_love(x, y, z):
	print "There are many reasons why I love her."
	print "Let me tell you three reasons why."
	print "I love her because she is so %s." % x
	print "I love her because she is so %s." % y
	print "I love her because she is so %s." % z
	
	
kate_love("beautiful", "sweet", "caring")
kate_love("thoughtful", "kind", "passionate")
kate_love("cute", "sexy", "fit")
kate_love("strong", "intelligent", "focused")
kate_love("fabulous", "interesting", "funny")
kate_love("shy", "lovely", "thick")
kate_love("adorable", "talented", "smart")
kate_love("amsuing", "attractive", "hot")
kate_love("cool", "independent", "pretty")
kate_love("fun", "gorgeous", "reliable")