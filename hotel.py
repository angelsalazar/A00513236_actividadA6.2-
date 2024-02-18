""" Hotel module """
import json


class Hotel:
    """ Hotel class """
    hotels_by_id = {}

    def __init__(self, name, number_of_rooms):
        """Constructor"""
        self.id = len(Hotel.hotels_by_id)
        self.name = name
        self.number_of_rooms = number_of_rooms
        self.reservations_by_id = {}

    def __str__(self):
        """Serialization to string"""
        return ','.join([
            f'id = {self.id}',
            f'name = {self.name}',
            f'number_of_rooms = {self.number_of_rooms}'
        ])

    def to_dict(self):
        """Serialization to dict"""
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['number_of_rooms'] = self.number_of_rooms
        return data

    def create_reservation(self, reservation):
        """create reservation"""
        self.reservations_by_id[reservation.id] = reservation

    def cancel_reservation(self, reservation_id):
        """cancel reservation"""
        if reservation_id not in self.reservations_by_id:
            print(f'reservation {reservation_id} not found')
            return None
        return self.reservations_by_id.pop(reservation_id)

    @staticmethod
    def create(name, number_of_rooms):
        """create hotel"""
        hotel = Hotel(name, number_of_rooms)
        Hotel.hotels_by_id[hotel.id] = hotel
        return hotel

    @staticmethod
    def delete(hotel_id):
        """delete hotel"""
        if hotel_id not in Hotel.hotels_by_id:
            print(f'hotel {hotel_id} not found')
            return None
        return Hotel.hotels_by_id.pop(hotel_id)

    @staticmethod
    def display(hotel_id):
        """display hotel"""
        if hotel_id not in Hotel.hotels_by_id:
            return None
        hotel = Hotel.hotels_by_id[hotel_id]
        print(hotel)
        return hotel

    @staticmethod
    def modify(hotel_id, name, number_of_rooms):
        """update hotel"""
        if hotel_id not in Hotel.hotels_by_id:
            print(f'hotel {hotel_id} not found')
            return None
        hotel = Hotel.hotels_by_id[hotel_id]
        hotel.name = name
        hotel.number_of_rooms = number_of_rooms
        Hotel.hotels_by_id[hotel.id] = hotel
        return hotel

    @staticmethod
    def save(file_name):
        """saves created hotels as json"""
        if file_name is None:
            file_name = 'hotels.json'
        records = []
        for entry in Hotel.hotels_by_id.items():
            records.append(Hotel.hotels_by_id[entry[1]].to_dict())
        with open(file_name, 'w', encoding='uft-8') as file:
            file.write(json.dumps(records))
