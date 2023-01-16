import gspread 
from google.oauth2.service_account import Credentials

import os
import colorama
from colorama import Fore
import sys
from termcolor import colored, cprint
import getch
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
ERROR = ''

def is_not_existing_user(input_username):
    """
    Checks if the user is new and gets called when the register option is sellected at the beginning of the programm
    """
    users = SHEET.worksheet('users-database')
    usernames = users.col_values(1)
    is_new_user = True
    for user in usernames:
        if input_username == user:
            print(user)
            is_new_user = False        
    return is_new_user
    

def create_password():
    """
    Will return a hashed password 
    """
    global ERROR
    
    password = ''
    while True:
        x = getch.getch()
        if x == '\r' or x == '\n':
            break
        print('*', end='', flush=True)
        password +=x
        
    encoded_psw = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded_psw, salt)
    print(hashed)
    return hashed
    print("\nout=", getPass()) 

    
def create_account():
    """
    Gets called when creating a new account
    """
    global ERROR
    username_input = input('create a unique username:\n')
    
    if is_not_existing_user(username_input) == True:
        print('great')
        credentials = [username_input, f'{create_password()}']
        users = SHEET.worksheet('users-database').append_row(credentials)
        
    else:
        ERROR = colored('this Username allready exists', 'red', attrs=['reverse', 'blink'])
        

def login():
    """
    Gets called when logging into an existing account
    """   
    username_input = input('feed your username to me:\n')
    

        
def auth():
    """
    auth will display input messages to the user to log into their account or create a new one
    with the appropriate exceptions and permissions
    """
    global ERROR
    
    print('1. Login')
    print('2. Register')
    user_auth_type = input('type one of the command numbers above in order to proceed \n')
    if user_auth_type == '2':
        create_account()
    elif user_auth_type == '1':
        login()
    else:
        ERROR = colored('please type in one of the two digit-options in the menu', 'red', attrs=['reverse', 'blink'])
        
        

def main():
    """
    Builds the app environment and calls all the functions and messages
    """
    global ERROR
    print(ERROR)
    print('This is a typing game to enhance your programming typing skills:')
   
    auth()
    
    
while True:
    #os.system('clear') 
    print('\n\n\n')
    main()
   








#NOTES

# text = colored('Hello, World!', 'yellow', attrs=['reverse', 'blink'])
# print(text)
# print(Fore.RED + 'This text is red in color')