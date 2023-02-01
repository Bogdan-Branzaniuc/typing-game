import gspread 
from google.oauth2.service_account import Credentials
import os
import colorama
from colorama import Fore 
from termcolor import colored, cprint
import sys
import getpass
import bcrypt
import pwinput

sys.path.append(os.path.abspath("assets/python-files"))
from typing_state import Typing_state
from game import Game
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
users_progress_db = SHEET.worksheet('users-progress')  
auth_object = Auth(users_db)
game = Game(users_progress_db, Typing_state)  
       
def main():
    """
    Builds the app environment and calls all the functions and messages
    """
    if auth_object.LOGGED_IN == False:
        title = colored('This is a typing game to enhance your programmer typing skills', 'yellow')
        print(title)
        auth_object.auth()
        game.connected_user = auth_object.user_name
        if game.connected_user not in users_progress_db.col_values(1):
            users_progress_db.append_row([game.connected_user])
    if auth_object.LOGGED_IN == True:
        if game.home_menu() == False:
            auth_object.LOGGED_IN = False  
        else:
            auth_object.LOGGED_IN = True

        
while True:
     main()   