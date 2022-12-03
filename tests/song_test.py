import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self): # this happens before every single test you run
        self.instance_of_song_1 = Song ("Kate Bush", "Hounds Of Love")
        self.instance_of_song_2 = Song ("Curtis Mayfield", "Move On Up")
        self.instance_of_song_3 = Song ("Mott the Hoople", "All the Young Dudes")

    def test_song_has_artist (self): 
        self.assertEqual("Kate Bush", self.instance_of_song_1.artist)

    def test_song_has_title (self): 
        self.assertEqual("Move On Up", self.instance_of_song_2.title)
