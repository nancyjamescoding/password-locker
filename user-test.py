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
def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'NancyNdungu')
        self.assertEqual(self.new_user.password,'XyZ3thf1')
def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
class TestDetails(unittest.TestCase):
    """
    A test class that defines test cases for details class
    """ 
    def setUp(self):
        """
        Method that runs before each individual ddetails test methods run.
        """
        self.new_details = Details('Gmail','nancy_ndungu','yx5Gij43')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'nancy_ndungu')
        self.assertEqual(self.new_credential.password,'yx5Gij43')
    
    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Details.details_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Details.details_list = []    
            
