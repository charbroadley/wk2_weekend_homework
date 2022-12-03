class Room:
    def __init__ (self, name, capacity, guests_in_room, playlist):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = guests_in_room
        self.playlist = playlist

    def check_guest_in_single (self, guest):
        self.guests_in_room.append(guest)

    def check_guest_in_multiple (self, guest_1, guest_2):
        self.guests_in_room.extend([guest_1, guest_2])

    def check_guest_out (self, guest):
        self.check_guest_in_single(guest)
        self.guests_in_room.remove(guest)
    
    def add_song_to_playlist (self, song):
        self.playlist.append(song)

# Error with this - come back to it later

#     def is_room_full (self, guest_1, guest_2, capacity):
#         self.check_guest_in_multiple(self, guest_1, guest_2)
#         if self.guests_in_room >= capacity:
#             return True
# # WIP
    # def name_of_guest_in_room (self, guest):
    #     self.add_guest_to_room(guest)
    #     return self.guests_in_room
