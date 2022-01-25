import unittest
from collections import UserList
from user import Details, User

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('NancyNdungu','XyZ3thf1')
