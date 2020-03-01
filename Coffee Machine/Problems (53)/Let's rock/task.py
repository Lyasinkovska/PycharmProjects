# start a RockBand here
class RockBand:
	genre = "rock"
	n_members = 4
	famous_songs = []

	def __init__(self, song):
		self.song = song


nightwish = RockBand
print(nightwish.genre)
print(nightwish.n_members)
print(nightwish.famous_songs)
