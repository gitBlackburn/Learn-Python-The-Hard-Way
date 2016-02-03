name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches 
weight = 180 #lbs 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name 
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffeee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, and %d I get %d." %(
	age, height, age + height + weight)
	
def pounds_to_kilos(pounds):
	kilos = pounds * 0.453592
	return kilos

print pounds_to_kilos(weight)

def inches_to_centimeters(inches):
	centimeters = inches * 2.54
	return centimeters 

print inches_to_centimeters(height)