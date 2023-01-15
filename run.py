import gspread 
from google.oauth2.service_account import Credentials

import curses
import os
from curses import wrapper
from curses.textpad import Textbox, rectangle

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3-users')

users = SHEET.worksheet('users-database') 
print(users)

print('This is a typing game to enhance your programming typing skills:')
#user_name = input('What is your username?\n')

# build the login logic
def auth():
    """
    auth will display input messages to the user to lig into their account or create a new one
    with the appropriate exceptions and permissions
    """    
    username = input("type in your username")
    

auth()

