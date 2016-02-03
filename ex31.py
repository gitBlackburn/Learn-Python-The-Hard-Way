print "You enter a dark room with two doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." %bear
	
elif door == "2":
	print "You stare into the endless abyss at Ctulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	print "4. This beat is, Bananas! B-A-N-A-N-A-S"
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The instanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "This is your type of heaven, before you there a three beautiful women."
	print "But you can only select one."
	print "Who do you select? The fat one, skinny one, or tall one?"
	
	girl = raw_input("> ")
	
	if girl == "tall" or girl =="tall one":
		print "She picks you up an gives you a kiss."
	elif girl == "fat" or girl == "fat one":
		print "She gives you a big bear hug."
	elif girl == "skinny" or girl == "skinny one":
		print "She looks at you for a moment and darts."
	else:
		print "All three girls vanish, oh well... more time for you to play Fallout 4 by yourself."
	
else:
	print "You stumble around and fall on a knife and die. Good job!"