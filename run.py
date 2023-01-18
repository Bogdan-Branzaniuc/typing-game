import gspread 
from google.oauth2.service_account import Credentials

import os
import colorama
from colorama import Fore
import sys
from termcolor import colored, cprint
import getpass
import pwinput
import bcrypt


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3-users')
ERROR = ' '
GREEN_MESSAGE = ' '
LOGGED_IN = False

def is_not_existing_user(input_username):
    """
    Checks if the user is new and gets called when the register option is sellected at the beginning of the programm
    """
    users = SHEET.worksheet('users-database')
    usernames = users.col_values(1)
    is_new_user = True
    for user in usernames:
        if input_username == user:
            is_new_user = False        
    return is_new_user
    

def create_password(salt):
    """
    Will return a hashed password 
    """  
    password = pwinput.pwinput(prompt ="", mask="*")        
    encoded_psw = password.encode('utf-8')
    hashed = bcrypt.hashpw(encoded_psw, salt)
    print('salt: ',salt)
    return hashed

    
def create_account():
    """
    Gets called when creating a new account
    """
    global ERROR
    global GREEN_MESSAGE
    username_input = input('create a unique username:\n')
    
    if is_not_existing_user(username_input) == True:
        print('Create a password')
        salt = bcrypt.gensalt()
        credentials = [username_input, f'{create_password(salt)}', f"{salt}"]
        users = SHEET.worksheet('users-database').append_row(credentials)
        GREEN_MESSAGE = colored('succesfully registered', 'green', attrs=['reverse', 'blink'])
        os.system('clear')
        ERROR =''
        print(GREEN_MESSAGE)
        main()        
        
    else:
        ERROR = colored('this Username allready exists', 'red', attrs=['reverse', 'blink'])
        os.system('clear')
        print(ERROR)
        create_account() #red-case recursive call to the same function. 

        
def login_check_password(db_user_password, user_salt):
    """
    Gets the user password and salt from the database and compares it to the user input for validation 
    """
    user_input_password =  f'{create_password(user_salt)}'  # bring the salt into the game for pasword matching
    if user_input_password != db_user_password:
        ERROR = colored('wrong password', 'red', attrs=['reverse', 'blink'])
        print(ERROR)
        login_check_password(db_user_password, user_salt) #red-case recursive call to the same function.
        
    
def login():
    """
    Gets called when logging into an existing account
    """   
    global ERROR
    global GREEN_MESSAGE
    global LOGGED_IN
    username_input = input('feed your username to me:\n')
    
    if is_not_existing_user(username_input) == False:
        users = SHEET.worksheet('users-database')
        usernames = users.col_values(1)
        passwords = users.col_values(2)
        salts = users.col_values(3)
        user_credentials = [[username, password, salt] for username, password, salt in zip(usernames,passwords, salts) if username_input == username][0]  #make a zip method and retrieve credentials
        print('type your password:')
        encoded_salt = user_credentials[2][2:-1].encode('utf-8')          
        login_check_password(user_credentials[1], encoded_salt)
        print('great Stuff you are now logged in') 
        GREEN_MESSAGE = colored('Successfuly logged in', 'green', attrs=['reverse', 'blink']) 
        ERROR =''
        os.system('clear')  
        LOGGED_IN = True
        print(GREEN_MESSAGE)
        main()       
    else:
        ERROR = colored('this Username does not exist', 'red', attrs=['reverse', 'blink'])
        os.system('clear')
        print(ERROR)
        login() #red-case recursive call to the same function. 

        
def auth():
    """
    auth will display input messages to the user to log into their account or create a new one
    with the appropriate exceptions and permissions
    """
    global ERROR
    global GEEN_MESSAGE
    global LOGGED_IN 
    print(ERROR)
    print('1. Login')
    print('2. Register')
    user_auth_type = input('type one of the command numbers above in order to proceed \n')
    if user_auth_type == '2':
        create_account()            
    elif user_auth_type == '1':
        login()     
    else:
        ERROR = colored('please type in one of the two digit-options in the menu', 'red', attrs=['reverse', 'blink'])
        
        
def game():
    """
    will hold the typing game curses code
    """
    print("let's begin the fun")
    
def main():
    """
    Builds the app environment and calls all the functions and messages
    """
    global LOGGED_IN
    if LOGGED_IN == False:
        print(ERROR)
        print('This is a typing game to enhance your programming typing skills:')
        auth()
    if LOGGED_IN == True:
        os.system('clear')
        print(GREEN_MESSAGE)
        print('This is a typing game to enhance your programming typing skills:')
        game()
        
          
print('\n\n\n')
main()
   








#NOTES

# text = colored('Hello, World!', 'yellow', attrs=['reverse', 'blink'])
# print(text)
# print(Fore.RED + 'This text is red in color')

# pygraph witht he dependencies / 3rd party loibraries
# technical design - flow 
# user manual - bullte points
# code Institute python validator.
# Unitesting 