from ast import While
import random
from user import Details, User

def create_new_user(username,password):
    '''
    Function creating  a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function that saves a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user =Details.verify_user(username,password)
    return check_user
def create_new_details(account,userName,password):
    """
    Function that creates new user details for a given user account
    """
    new_credential = Details(account,userName,password)
    return new_credential
def save_details(details):
    """
    Function to save Credentials to the credentials list
    """
    details. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Details.display_details()

def delete_details(details):
    """
    Function to delete a Credentials from credentials list
    """
    details.delete_details()

def find_details(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Details.find_details(account)
def check_deatils(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Details.if_details_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Details.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Details.copy_password(account)


def main():

    while True:

        print("welcome to password locker: to create new user enter'nu':To login 'lg': or 'ex' to exit the system ")
        print('\n')
        print("select a short code to navigate through")
        short_code=input().lower()
        print('\n')


        if short_code == 'nu':
            print ('Sign Up')
            print('*' * 50)
            username = input('username: ')
            while True:
                print("To Enter password 'et' :\n 'GP'To generate random Password")
                choose_password = input().lower().strip()
                if choose_password == 'et':
                    password = input("Enter Password\n")
                    break
                    
                elif choose_password == 'gp':
                    password = generate_Password()
                    break  
            else:
                print("Invalid password please try again")
            save_user(create_new_user(username,password))
            print("*"*50)
            print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
            print("*"*50)
        elif short_code == "lg":
            print("*"*100)
            print("Enter your User name and your Password to log in:")
            print('*' * 50)
            username = input("User name: ")
            password = input("password: ")
            login = login_user(username,password)
            if login_user == login:
               print(f"Hello {username}.Welcome To PassWord Locker")  
               print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_details(search_name):
                search_details = find_details(search_name)
                print(f"Account Name : {search_details.account}")
                print('-' * 50)
                print(f"User Name: {search_details.userName} Password :{search_details.password}")
                print('-' * 50)
            else:
                print("Details do not exist")
                print('\n')   
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_details(search_name):
                search_credential = find_details(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry, Check your entry again and let it match those in the menu")
    else:
            print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()    

                    




                   

                



