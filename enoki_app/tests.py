import unittest

from django.test import TestCase

# Create your tests here.


class TestClass(unittest.TestCase):

    stuff = {
        'id': 1,
        'first_name': 'William',
        'last_name': 'Barillon'
    }

    def testDataSuccess(self):
        self.assertEqual(self.stuff['first_name'], 'William')

    def testDataFail(self):
        self.assertNotEqual('William2', 'William')