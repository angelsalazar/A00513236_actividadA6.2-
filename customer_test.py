import unittest
import os
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Customer.customers_by_id = {}

    def tearDown(self):
        if os.path.exists('customers_test.json'):
            os.remove('customers_test.json')

    def test_create_customer(self):
        c = Customer.create('John Doe', 'john@doe.com')
        self.assertIsNotNone(c.id)
        self.assertEqual('John Doe', c.name)
        self.assertEqual('john@doe.com', c.email)
        self.assertEqual(1, len(Customer.customers_by_id))

    def test_delete_customer(self):
        h1 = Customer.create('John Doe', 'john@doe.com')
        h2 = Customer.create('Jane Doe', 'jane@doe.com')

        self.assertEqual(2, len(Customer.customers_by_id))
        deleted_customer = Customer.delete(h1.id)

        self.assertEqual(h1.name, deleted_customer.name)
        self.assertEqual(1, len(Customer.customers_by_id))

        Customer.delete(20)
        self.assertEqual(1, len(Customer.customers_by_id))
    
    def test_display_customer(self):
        Customer.create('Jane Doe', 'jane@doe.com')
        h = Customer.display(0)
        self.assertEqual('Jane Doe', h.name)
        self.assertEqual('jane@doe.com', h.email)

        h = Customer.display(10)
        self.assertIsNone(h)

    def test_modify_customer(self):
        Customer.create('Jane Doe', 'jane@doe.com')
        Customer.modify(0, 'Jane Doe Updated', 'jane.updated@doe.com')

        h = Customer.display(0)
        self.assertEqual('Jane Doe Updated', h.name)
        self.assertEqual('jane.updated@doe.com', h.email)

        h = Customer.modify(20, 'Random user', 'random.user@doe.com')
        self.assertIsNone(h)

    def test_save(self):
        Customer.create('Jane Doe', 'jane@doe.com')
        Customer.create('John Doe', 'john@doe.com')
        
        file_name = 'customers_test.json'

        Customer.save(file_name)

        with open(file_name, 'r') as file:
            self.assertIsNotNone(file)

if __name__ == '__main__':
    unittest.main()