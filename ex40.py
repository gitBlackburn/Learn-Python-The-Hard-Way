class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there"])
				
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
day_o = Song(["Day light come and me  want to go home",
			"Day light come and me want to go home"])
			
mary_had_a_lil_lamb = Song(["Mary had a little lamb",
							"Little lamb, little lamb"])
							
day_o.sing_me_a_song()
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()



