class Guest:
    def __init__ (self, name, favourite_song):
        self.name = name
        self.favourite_song = favourite_song

    def favourite_song_woohoo (self, guest, song):
        if guest.favourite_song.title == song.title:
            return "Woohoo! This is my favourite song!"
        else:
            return "I don't like this song"

    def favourite_artist(self, guest, song):
        if guest.favourite_song.artist == song.artist:
            return f"I love {song.artist}!!"
        else:
            return f"Nah, I don't like {song.artist}"
