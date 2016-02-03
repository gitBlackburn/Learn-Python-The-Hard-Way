tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm\\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

# makes a spinning bar but causes a loss of powershell control
# while i < 10:
	# for i in ["/","-","|","\\","|"]:
		# print "%s\r" % i,
		
# escape sequences test
print "\\"
print '\''
print "\""
ten = 10
#print "\a" # makes a ping sound but does not print anything
print "hi\bhello %d" % 10
print "what\fwhat" 
print "\N{blue}"
print "nam0\rnam1"
print "Hello\vworld!"

x = "\"What am I doing? Who\'s is this?\""
y = "What's the matter?"

print "%r" % x
print "%s" % x