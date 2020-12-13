class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
happy_bday = Song(["Happy Bday to you",
                   "I dont want to get sued"
				   "So I will stop right there"])
bulls_on_parade = Song(["They rally around the family",
                        "with pocket full of shells"])
                        
song_lyrics = "Will stay forever this way..and you here in my heart and my heart will go on and on.."
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
happy_bday1 = Song(song_lyrics)
happy_bday1.sing_me_a_song()