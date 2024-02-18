""" Customer module """
import json


class Customer:
    """ Customer class """
    customers_by_id = {}

    def __init__(self, name, email):
        """ constructor """
        self.id = len(Customer.customers_by_id)
        self.name = name
        self.email = email

    def __str__(self):
        """ string serialization """
        return f'id = {self.id}, name = {self.name}, email = {self.email}'

    def to_dict(self):
        """ dict serialization """
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['email'] = self.email
        return data

    @staticmethod
    def create(name, email):
        """ create customer """
        customer = Customer(name, email)
        Customer.customers_by_id[customer.id] = customer
        return customer

    @staticmethod
    def delete(customer_id):
        """ delete customer """
        if customer_id not in Customer.customers_by_id:
            print(f'customer {customer_id} not found')
            return None
        return Customer.customers_by_id.pop(customer_id)

    @staticmethod
    def display(customer_id):
        """ display customer """
        if customer_id not in Customer.customers_by_id:
            print(f'customer {customer_id} not found')
            return None
        customer = Customer.customers_by_id[customer_id]
        print(customer)
        return customer

    @staticmethod
    def modify(customer_id, name, email):
        """ modify customer """
        if customer_id not in Customer.customers_by_id:
            print(f'customer {customer_id} not found')
            return None
        customer = Customer.customers_by_id[customer_id]
        customer.name = name
        customer.email = email
        Customer.customers_by_id[customer.id] = customer
        return customer

    @staticmethod
    def save(file_name):
        """save created customers as json"""
        if file_name is None:
            file_name = 'customers.json'

        records = []
        for entry in Customer.customers_by_id.items():
            records.append(Customer.customers_by_id[entry[1]].to_dict())
        with open(file_name, 'w', encoding='uft-8') as file:
            file.write(json.dumps(records))
