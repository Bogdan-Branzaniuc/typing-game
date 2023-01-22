import gspread 
from google.oauth2.service_account import Credentials
import os
import colorama
from colorama import Fore 
import sys
from termcolor import colored, cprint
import getpass
import bcrypt
import pwinput


sys.path.append(os.path.abspath("assets/python-files"))
from game_state import Game
from auth import Auth


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3-users')

users_db = SHEET.worksheet('users-database')  
auth_object = Auth(Game,users_db)
game_state = Game(auth_object, users_db)  
       
def main():
    """
    Builds the app environment and calls all the functions and messages
    """
    print('This is a typing game to enhance your programmer typing skills:')
    
    if auth_object.LOGGED_IN == False:
        auth_object.auth()
    if auth_object.LOGGED_IN == True:
        game_state.home_menu()


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