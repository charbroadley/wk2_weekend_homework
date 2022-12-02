import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self): # this happens before every single test you run
        self.instance_of_guest_1 = Guest ("Laura")
        self.instance_of_guest_2 = Guest ("Ian")
        self.instance_of_guest_3 = Guest ("Charlotte")
        self.instance_of_guest_4 = Guest ("Millie")

    def test_guest_name_1 (self): 
        self.assertEqual("Laura", self.instance_of_guest_1.name)

    def test_guest_name_3 (self): 
        self.assertEqual("Charlotte", self.instance_of_guest_3.name)
