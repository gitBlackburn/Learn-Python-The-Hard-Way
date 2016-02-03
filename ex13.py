from sys import argv

script, first, second, third, forth = argv

print "The script is called:", script
print "Your first varible is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "How old are you?", forth
age = raw_input()
print "You are %s years old." % age