import unittest
import os
from reservation import Reservation
from hotel import Hotel
from customer import Customer

class TestHotel(unittest.TestCase):
    def setUp(self):
        Reservation.reservations_by_id = {}

    def tearDown(self):
        if os.path.exists('reservations_test.json'):
            os.remove('reservations_test.json')

    def test_create_reservartion(self):
        hotel = Hotel.create('demo', 20)
        customer = Customer.create('Jane Doe', 'jane@doe.com')
        reservation = Reservation.create(customer, hotel)
        self.assertIsNotNone(reservation.id)
        self.assertEqual(1, len(hotel.reservations_by_id))

    def test_cancel_reservartion(self):
        hotel = Hotel.create('demo', 20)
        customer = Customer.create('Jane Doe', 'jane@doe.com')
        reservation = Reservation.create(customer, hotel)
        
        deleted_reservation = Reservation.cancel(reservation.id, hotel)
        self.assertEqual(deleted_reservation.id, reservation.id)
        self.assertEqual(0, len(hotel.reservations_by_id))
    
    def test_save(self):
        hotel = Hotel.create('demo', 20)
        customer = Customer.create('Jane Doe', 'jane@doe.com')
        reservation = Reservation.create(customer, hotel)
        
        file_name = 'reservations_test.json'
        Reservation.save(file_name)

        with open(file_name, 'r') as file:
            self.assertIsNotNone(file)

if __name__ == '__main__':
    unittest.main()
