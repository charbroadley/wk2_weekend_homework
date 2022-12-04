import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self): # this happens before every single test you run
        self.instance_of_song_1 = Song ("Kate Bush", "Hounds Of Love")
        self.instance_of_song_2 = Song ("Curtis Mayfield", "Move On Up")
        self.instance_of_song_3 = Song ("Mott the Hoople", "All the Young Dudes")
        playlist = [self.instance_of_song_1, self.instance_of_song_3]
        guests_in_room = []
        self.instance_of_room = Room ("The Bowie", 2, guests_in_room, playlist, 10)
        self.instance_of_guest_1 = Guest ("Ian", self.instance_of_song_1, 20)
        self.instance_of_guest_2 = Guest ("Laura", self.instance_of_song_2, 5)
        self.instance_of_guest_3 = Guest ("Charlotte", self.instance_of_song_3, 15)
        
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
        self.assertEqual(3, len(self.instance_of_room.playlist))

    def test_room_capacity_space (self):
        party_people = [self.instance_of_guest_1]
        room_at_capacity = self.instance_of_room.is_room_full (party_people, self.instance_of_room.capacity)
        self.assertEqual(False, room_at_capacity)
    
    def test_room_capacity_full (self):
        party_people = [self.instance_of_guest_1, self.instance_of_guest_2]
        room_at_capacity = self.instance_of_room.is_room_full (party_people, self.instance_of_room.capacity)
        self.assertEqual(True, room_at_capacity)

    def test_room_full_message_for_guest(self):
        party_people = [self.instance_of_guest_1, self.instance_of_guest_2]
        room_at_capacity = self.instance_of_room.room_full_message(party_people, self.instance_of_room.capacity,self.instance_of_guest_3)
        self.assertEqual("No party for you!", room_at_capacity)

    def test_room_not_full_message_for_guest (self):
        party_people = [self.instance_of_guest_1]
        room_at_capacity = self.instance_of_room.room_full_message(party_people, self.instance_of_room.capacity,self.instance_of_guest_3)
        self.assertEqual("Party timmeee!!!", room_at_capacity)

    def test_guest_can_pay_entry_fee (self):
        enough_money = self.instance_of_room.guest_has_enough_money(self.instance_of_guest_1)
        self.assertEqual("Enter", enough_money)

    def test_guest_cant_pay_entry_fee (self):
        enough_money = self.instance_of_room.guest_has_enough_money(self.instance_of_guest_2)
        self.assertEqual("No Entry", enough_money)