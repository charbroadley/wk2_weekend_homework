import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self): # this happens before every single test you run
        self.instance_of_song_1 = Song ("Kate Bush", "Hounds Of Love")
        self.instance_of_song_2 = Song ("Curtis Mayfield", "Move On Up")
        self.instance_of_song_3 = Song ("Mott the Hoople", "All the Young Dudes")
        self.instance_of_guest_1 = Guest ("Ian", self.instance_of_song_1)
        self.instance_of_guest_2 = Guest ("Laura", self.instance_of_song_2)
        self.instance_of_guest_3 = Guest ("Charlotte", self.instance_of_song_3)
        

    def test_guest_name_1 (self): 
        self.assertEqual("Ian", self.instance_of_guest_1.name)

    def test_guest_name_3 (self): 
        self.assertEqual("Charlotte", self.instance_of_guest_3.name)

    def test_guest_has_favourite_song (self):
        self.assertEqual("All the Young Dudes", self.instance_of_guest_3.favourite_song.title)

    def test_guest_has_favourite_song_woohoo_matching(self):
        favourite = self.instance_of_guest_2.favourite_song_woohoo(self.instance_of_guest_2, self.instance_of_song_2)
        self.assertEqual("Woohoo! This is my favourite song!", favourite)

    def test_guest_has_favourite_song_woohoo_not_matching(self):
        not_favourite = self.instance_of_guest_1.favourite_song_woohoo(self.instance_of_guest_1, self.instance_of_song_3)
        self.assertEqual("I don't like this song", not_favourite)

    def test_guest_loves_this_artist_matching (self):
        love_them = self.instance_of_guest_3.favourite_artist (self.instance_of_guest_3, self.instance_of_song_3)
        self.assertEqual("I love Mott the Hoople!!", love_them)
        
    def test_guest_loves_this_artist_not_matching (self):
        dont_love_them = self.instance_of_guest_2.favourite_artist (self.instance_of_guest_2, self.instance_of_song_1)
        self.assertEqual("Nah, I don't like Kate Bush", dont_love_them)