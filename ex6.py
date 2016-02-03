# Asssigns a string to the varibale x
x = "There are %d types of people." %10
# Assigns a string to binary
binary = "binary"
# Assigns a string to do_not 
do_not = "don't"
# Assigns a string to the variable y and makes use of conversion
y = "Those who know %s and those who %s." %(binary, do_not)

# prints x
print x 
#prints y
print y

# Repeats first line with I said added to the front 
print "I said: %r." %x
# Repeats the second line with I also said added to the front of the line
print "I also said: '%s'." %y

# Assigns hilarious the boolean value of False
hilarious = False
# assigns joke_evaluation to the screen
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evaluation then hilarious on the same line
print joke_evaluation % hilarious

# assigns a string to w
w = "This is the left side of..."
# assigns a string to e
e = "a string with a right side."

# prints w then e, on the same line
print w + e