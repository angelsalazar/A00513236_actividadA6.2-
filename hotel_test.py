import unittest
import os
from hotel import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        Hotel.hotels_by_id = {}

    def tearDown(self):
        if os.path.exists('hotels_test.json'):
            os.remove('hotels_test.json')

    def test_create_hotel(self):
        h = Hotel.create('random hotel', 10)
        self.assertIsNotNone(h.id)
        self.assertEqual('random hotel', h.name)
        self.assertEqual(10, h.number_of_rooms)
        self.assertEqual(1, len(Hotel.hotels_by_id))

    def test_delete_hotel(self):
        h1 = Hotel.create('A hotel', 10)
        h2 = Hotel.create('B hotel', 20)

        self.assertEqual(2, len(Hotel.hotels_by_id))
        deleted_hotel = Hotel.delete(h1.id)

        self.assertEqual(h1.name, deleted_hotel.name)
        self.assertEqual(1, len(Hotel.hotels_by_id))

        Hotel.delete(20)
        self.assertEqual(1, len(Hotel.hotels_by_id))
    
    def test_display_hotel(self):
        Hotel.create('C hotel', 10)
        h = Hotel.display(0)
        self.assertEqual('C hotel', h.name)
        self.assertEqual(10, h.number_of_rooms)

        h = Hotel.display(10)
        self.assertIsNone(h)

    def test_modify_hotel(self):
        Hotel.create('C hotel', 10)
        Hotel.modify(0, 'Updated C hotel', 20)

        h = Hotel.display(0)
        self.assertEqual('Updated C hotel', h.name)
        self.assertEqual(20, h.number_of_rooms)

        h = Hotel.modify(20, 'Updated C hotel', 20)
        self.assertIsNone(h)

    def test_save(self):
        Hotel.create('A hotel', 20)
        Hotel.create('C hotel', 10)
        
        file_name = 'hotels_test.json'

        Hotel.save(file_name)

        with open(file_name, 'r') as file:
            self.assertIsNotNone(file)

if __name__ == '__main__':
    unittest.main()
