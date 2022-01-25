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
    




 





