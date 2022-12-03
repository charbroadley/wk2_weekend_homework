import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self): # this happens before every single test you run
        self.instance_of_song_1 = Song ("Kate Bush", "Hounds Of Love")
        self.instance_of_song_2 = Song ("Curtis Mayfield", "Move On Up")
        playlist = [self.instance_of_song_1]
        guests_in_room = []
        self.instance_of_room = Room ("The Bowie", 2, guests_in_room, playlist)
        self.instance_of_guest_1 = Guest ("Ian", self.instance_of_song_1)
        self.instance_of_guest_2 = Guest ("Laura", self.instance_of_song_2)
        
    def test_room_has_name (self):
        self.assertEqual("The Bowie", self.instance_of_room.name)

    def test_check_room_has_capacity (self):
        self.assertEqual (2, self.instance_of_room.capacity)

    def test_can_check_guest_in_single (self):
        self.instance_of_room.check_guest_in_single (self.instance_of_guest_1)
        self.assertEqual (1, len(self.instance_of_room.guests_in_room))

    def test_can_check_guest_in_multiple (self):
        self.instance_of_room.check_guest_in_multiple (self.instance_of_guest_1, self.instance_of_guest_2)
        self.assertEqual (2, len(self.instance_of_room.guests_in_room)) 

    def test_can_check_guest_out (self):
        self.instance_of_room.check_guest_out (self.instance_of_guest_1)
        self.assertEqual(0, len(self.instance_of_room.guests_in_room))

    def test_add_song_to_room (self):
        self.instance_of_room.add_song_to_playlist (self.instance_of_song_2)
        self.assertEqual(2, len(self.instance_of_room.playlist))

# TypeError: Room.is_room_full() takes 4 positional arguments but 5 were given

    # def test_is_room_full (self):
    #     capacity = 2
    #     full_room = self.instance_of_room.is_room_full (self, self.instance_of_guest_1, self.instance_of_guest_2, capacity)
    #     self.assertEqual(True, full_room)

# WIP
    # def test_find_guest_in_room_by_name (self):
    #     guest = self.instance_of_room.name_of_guest_in_room(self.instance_of_guest)
    #     self.assertEqual ("Charlotte", self.instance_of_room.guests_in_room)
