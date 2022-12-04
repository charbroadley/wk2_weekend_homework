class Guest:
    def __init__ (self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def favourite_song_woohoo (self, guest, song):
        if guest.favourite_song.title == song.title:
            return "Woohoo! This is my favourite song!"
        else:
            return "I don't like this song"

    # def guest_favourite_song_on_room_playlist (self, guest, room):
    #     for song in room.playlist:
    #         if guest.favourite_song == room.playlist:
    #             return "Woohoo!!"
    #     return "Urgh!!"

    def favourite_artist(self, guest, song):
        if guest.favourite_song.artist == song.artist:
            return f"I love {song.artist}!!"
        else:
            return f"Nah, I don't like {song.artist}"

    def wallet_decreases (self, guest, entry_fee):
        guest.wallet -= entry_fee
        return guest.wallet
        

        
