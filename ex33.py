i = 0
numbers = []

# def choice(loop_num, inc):
	# global i 
	# while i < loop_num:
		# print "At the top i is %d" %i
		# numbers.append(i)
		
		# i = i + inc
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d" %i 
	
	
# print "The numbers: "

for i in range(0, 6):
	print "At the top i is %d" %i
	numbers.append(i)
		
	# i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" %i 

# choice(100, 5)

for num in numbers:
	print num