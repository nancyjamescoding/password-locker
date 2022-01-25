import random
import string

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
    




 





