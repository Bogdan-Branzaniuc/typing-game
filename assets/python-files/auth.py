import pwinput
import bcrypt
import os
import colorama
from colorama import Fore 
from termcolor import colored, cprint
class Auth:
    def __init__(self, users_db):
        self.LOGGED_IN = False
        self.users_credentials = users_db

    
    def is_not_existing_user(self, input_username):
        """
        Checks if the user is new and gets called when the register option is sellected at the beginning of the programm
        """
        usernames = self.users_credentials.col_values(1)
        is_new_user = True
        for user in usernames:
            if input_username == user:
                is_new_user = False        
        return is_new_user
        

    def create_password(self, salt):
        """
        Will return a hashed password 
        """  
        password = pwinput.pwinput(prompt=f"{colored('Password:', 'cyan')}", mask="*")        
        encoded_psw = password.encode('utf-8')
        hashed = bcrypt.hashpw(encoded_psw, salt)
        return hashed

        
    def create_account(self):
        """
        Gets called when creating a new account
        uses is_not_existing_user function for the username duplicate red case
        """
        username_input = input(f"{colored('Create a unique username:', 'cyan')}")
        
        if self.is_not_existing_user(username_input) == True:
            salt = bcrypt.gensalt()
            credentials = [username_input, f'{self.create_password(salt)}', f"{salt}"]
            users = self.users_credentials.append_row(credentials)
            GREEN_MESSAGE = colored('succesfully registered', 'green', attrs=['reverse', 'blink'])
            os.system('clear')
            print(GREEN_MESSAGE)       
        else:
            ERROR = colored('this Username allready exists', 'red', attrs=['reverse', 'blink'])
            print(ERROR)
            self.create_account()  

            
    def login_check_password(self, db_user_password, user_salt):
        """
        Gets the user password and salt from the database and compares it to the user input for validation 
        """
        user_input_password =  f'{self.create_password(user_salt)}'
        if user_input_password != db_user_password:
            ERROR = colored('wrong password', 'red', attrs=['reverse', 'blink'])
            print(ERROR)
            self.login_check_password(db_user_password, user_salt) 
            
        
    def login(self):
        """
        Gets called when logging into an existing account
        """   
        username_input = input(f"{colored('type your username in:', 'cyan')}")
        if self.is_not_existing_user(username_input) == False:
            usernames = self.users_credentials.col_values(1)
            passwords = self.users_credentials.col_values(2)
            salts = self.users_credentials.col_values(3)
            user_credentials = [[username, password, salt] for username, password, salt in 
                                zip(usernames,passwords, salts) if username_input == username][0]  
            encoded_salt = user_credentials[2][2:-1].encode('utf-8')          
            self.login_check_password(user_credentials[1], encoded_salt)
            GREEN_MESSAGE = colored('Successfuly logged in', 'green', attrs=['reverse', 'blink']) 
            os.system('clear')
            print(GREEN_MESSAGE) 
            self.LOGGED_IN = True 
        else:
            ERROR = colored('this Username does not exist', 'red', attrs=['reverse', 'blink'])
            print(ERROR)
            self.login() 

            
    def auth(self):
        """
        auth will display input messages to the user to log into their account or create a new one
        with the appropriate exceptions and permissions
        automatically loggs the user out, since no operation needed after log-in requires the auth function
        """
        
        print('1. Login')
        print('2. Register')
        user_auth_input_instruction = colored('type one of the command numbers above in order to proceed \n', 'cyan')
        user_auth_input = input(f'{user_auth_input_instruction}')
        
        if user_auth_input == '2':
            self.create_account()            
        elif user_auth_input == '1':
            self.login()     
        else:
            ERROR = colored('please type in one of the options in the menu', 'red', attrs=['reverse', 'blink']) 
            print(ERROR)