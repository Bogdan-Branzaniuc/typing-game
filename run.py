import gspread
from google.oauth2.service_account import Credentials
import colorama
import os
import time
from colorama import Fore
from termcolor import colored

from typing_state import Typing_state
from game import Game
from auth import Auth

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("project3-users")

users_db = SHEET.worksheet("users-database")
users_progress_db = SHEET.worksheet("users-progress")
auth_object = Auth(users_db)
game = Game(users_progress_db, Typing_state)


def main():
    """
    Builds the app environment and calls all the functions and messages
    """
    if auth_object.logged_in:
        if game.home_menu() == False:
            auth_object.logged_in = False
        else:
            auth_object.logged_in = True
    else:
        title = """
 ____  __.                _____         .__   __                
|    |/ _|____ ___.__.   /     \   ____ |  |_/  |_  ___________ 
|      <_/ __ <   |  |  /  \ /  \_/ __ \|  |\   __\/ __ \_  __ \ 
|    |  \  ___/\___  | /    Y    \  ___/|  |_|  | \  ___/|  | \/
|____|__ \___  > ____| \____|__  /\___  >____/__|  \___  >__|   
        \/   \/\/              \/     \/               \/       
"""
        print(colored(title,'green'))
        title_text = "This is a programm to enhance your typing skills"
        title = colored(title_text, "yellow")
        print(title)
        auth_object.auth()
        game.connected_user = auth_object.user_name
        if game.connected_user not in users_progress_db.col_values(1):
            users_progress_db.append_row([game.connected_user])


while True:
    main()
    
