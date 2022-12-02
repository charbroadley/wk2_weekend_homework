import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self): # this happens before every single test you run
        self.instance_of_song_1 = Song ("Paramore", "Misery Business")
        self.instance_of_song_2 = Song ("Kate Bush", "Hounds Of Love")
        self.instance_of_song_3 = Song ("Curtis Mayfield", "Move On Up")
        self.instance_of_song_4 = Song ("Taylor Swift", "Shake It Off")

    def test_song_has_artist (self): 
        self.assertEqual("Kate Bush", self.instance_of_song_2.artist)

    def test_song_has_title (self): 
        self.assertEqual("Shake It Off", self.instance_of_song_4.title)
