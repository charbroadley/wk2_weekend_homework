class Room:
    def __init__ (self, name, capacity, guests_in_room, playlist, entry_fee):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = guests_in_room
        self.playlist = playlist
        self.entry_fee = entry_fee

    def check_guest_in_single (self, guest):
        self.guests_in_room.append(guest)

    def check_guest_in_multiple (self, guest_1, guest_2):
        self.guests_in_room.extend([guest_1, guest_2])

    def check_guest_out (self, guest):
        self.check_guest_in_single(guest)
        self.guests_in_room.remove(guest)
    
    def add_song_to_playlist (self, song):
        self.playlist.append(song)

    def is_room_full (self, guests, capacity):
        if len(guests) >= self.capacity:
            return True
        else:
            return False

    def room_full_message (self,guests, capacity, new_guest):
        if self.is_room_full(guests, capacity) == True:
            return "No party for you!"
        else:
            return "Party timmeee!!!"

    def guest_has_enough_money (self,guest):
        if guest.wallet >= self.entry_fee:
            return "Enter"
        else:
            return "No Entry"
