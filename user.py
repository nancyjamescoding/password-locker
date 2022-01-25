import random
import string
# import pyperclip

class User:
    '''
    class that generates an instance of the user
    '''
    
    user_list=[]

    def __init__(self, user_name, password):

        '''
        method that defines properties of a user
        '''
        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        method that saves new user instance to the users list
        '''

        User.user_list.append(self)

    @classmethod
    def display_user(cls):
      return cls.user_list

    def delete_user(self):
      '''
      deletes a saved account from the list
      '''
      User.user_list.remove(self)

class  Details:
    '''
    class that generates an instance of the user's details
    '''   
    details_list=[]

    @classmethod
    def verify_user(cls,username,password):
        '''
        method to verify user in the list
        '''
        a_user = ''
        for user in User.user_list:
            if (user.username == username and password.password == password):
                a_user == user.username
        return a_user
    def __init__(self,account,username, password):
        '''
        method that defines the details to be saved
        '''
        self.account = account
        self.username = username
        self.password  = password

    def save_details(self):
        '''
        method that saves details of a new user
        '''     
        Details.details_list.append(self) 

    def delete_details(self):
        '''
        method that deletes saved details of a user
        '''
        Details.details_list.remove(self)

    @classmethod
    def find_details(cls,account):
        '''

        '''
        for detail in Details.details_list:
            if detail.account == account:
                return detail

    # @classmethod
    # def copy_password(cls,account):
    #     ''''

    #     '''  
    #     found_details = Details.find_details(account)
    #     pyperclip.copy(found_details.password)

    @classmethod
    def details_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for detail in cls.details_list:
            if detail.account == account:
                return True
        return False
    @classmethod
    def display_details(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.details_list

    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
    




 





