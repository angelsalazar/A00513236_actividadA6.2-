""" Reservation module """
import json


class Reservation:
    """ Reservation class """
    reservations_by_id = {}

    def __init__(self, customer_id, hotel_id):
        """ constructor """
        self.id = len(Reservation.reservations_by_id)
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def __str__(self):
        """ string serialization """
        return ','.join([
            f'id = {self.id}',
            f'customer_id = {self.customer_id}',
            f'hotel_id = {self.hotel_id}',
        ])

    def to_dict(self):
        """ dict serialization """
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'hotel_id': self.hotel_id
        }

    @staticmethod
    def create(customer, hotel):
        """ create reservation """
        booking = Reservation(customer.id, hotel.id)
        Reservation.reservations_by_id[booking.id] = booking
        hotel.create_reservation(booking)
        return booking

    @staticmethod
    def cancel(reservation_id, hotel):
        """ cancel reservation """
        booking = hotel.cancel_reservation(reservation_id)
        if booking is not None:
            Reservation.reservations_by_id.pop(booking.id)
        return booking

    @staticmethod
    def save(file_name):
        """ save created reservations to json file """
        if file_name is None:
            file_name = 'reservations.json'

        records = []
        for entry in Reservation.reservations_by_id:
            records.append(Reservation.reservations_by_id[entry[1]].to_dict())
        with open(file_name, 'w', encoding='uft-8') as file:
            file.write(json.dumps(records))
