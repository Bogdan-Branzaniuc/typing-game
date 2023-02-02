import pwinput
import bcrypt
import os
import colorama
from colorama import Fore
from termcolor import colored

MINIMUM_AUTH_INPUT = 3


class Auth:
    def __init__(self, users_db):
        self.logged_in = False
        self.users_credentials = users_db
        self.user_name = ""
        self.MINIMUM_AUTH_INPUT = 3

    def is_existing_user(self, input_username, register_or_login):
        """
        Checks if the user is new and prints an error if it isn't.
        the register_or_login parameter checkes where the function is used,
        so it only displays a registration error in a register context, while
        being used for a login functionality as well
        """
        usernames = self.users_credentials.col_values(1)
        is_current_user = False
        for user in usernames:
            if input_username == user:
                is_current_user = True
                if register_or_login == "register":
                    error = colored("this Username allready exists", "red")
                    print(error)
                    
        return is_current_user

    def auth_field_min_3_char(self, user_input, min_len=MINIMUM_AUTH_INPUT):
        """
        Checkes if an input field is at least 3 characters long and prints an error if it isn't
        """
        if len(user_input) < min_len:
            error = colored("this field should be at least 3 characters long", "red")
            print(error)
            return False
        else:
            return True

    def create_password(self, salt):
        """
        Will return a hashed password
        """
        password = pwinput.pwinput(prompt=f"{colored('Password:', 'cyan')}", mask="*")  
       
        if self.auth_field_min_3_char(password) == True:
            encoded_psw = password.encode("utf-8")
            hashed = bcrypt.hashpw(encoded_psw, salt)
            return hashed
        else:
            return self.create_password(salt)

    def create_account(self):
        """
        Gets called when creating a new account
        uses is_existing_user function for the username duplicate red case
        """
        username_input = input(f"{colored('Create a unique username:', 'cyan')}")

        if (
            self.is_existing_user(username_input, "register") == False
            and self.auth_field_min_3_char(username_input) == True
        ):
            salt = bcrypt.gensalt()
            credentials = [username_input, f"{self.create_password(salt)}", f"{salt}"]
            users = self.users_credentials.append_row(credentials)
            green_messaage = colored("succesfully registered", "green")
            os.system('clear')
            print(green_messaage)
        else:
            self.create_account()

    def login_check_password(self, db_user_password, user_salt):
        """
        Gets the user password and salt from the database and compares it to the user input for validation
        handles the exit option if tiped in the password field
        """
        user_input_password = f"{self.create_password(user_salt)}"

        exit = 'exit'
        encoded_exit = exit.encode("utf-8")
        exit_hashed = bcrypt.hashpw(encoded_exit, user_salt)
        
        if str(user_input_password) == str(exit_hashed):
            self.auth() 
        elif user_input_password != db_user_password:
            error = colored("wrong password", "red")
            print(error)
            self.login_check_password(db_user_password, user_salt)

    def login(self):
        """
        Gets called when logging into an existing account
        """
        input_message = (
            colored("type ", "cyan")
            + colored("exit ", "red")
            + colored("into any field to go back \n", "cyan")
        )
        input_message += colored("username:", "cyan")
        username_input = input(input_message)
        if username_input == "exit":
            self.auth()
        elif self.is_existing_user(username_input, "login") == True:
            usernames = self.users_credentials.col_values(1)
            passwords = self.users_credentials.col_values(2)
            salts = self.users_credentials.col_values(3)
            user_credentials = [
                [username, password, salt]
                for username, password, salt in zip(usernames, passwords, salts)
                if username_input == username
            ][0]
            encoded_salt = user_credentials[2][2:-1].encode("utf-8")
            self.login_check_password(user_credentials[1], encoded_salt)
            green_messaage = colored("Successfuly logged in", "green")
            os.system("clear")
            print(green_messaage)
            self.logged_in = True
            self.user_name = username_input
            
        else:
            error = colored("this Username does not exist", "red")
            print(error)
            self.login()

    def auth(self):
        """
        auth will display input messages to the user to log into their account or create a new one
        with the appropriate exceptions and permissions
        automatically loggs the user out, since no operation needed after log-in requires the auth function
        """

        print("1. Login")
        print("2. Register")
        user_auth_input_instruction = colored(
            "type one of the command numbers above in order to proceed \n", "cyan"
        )
        user_auth_input = input(f"{user_auth_input_instruction}")

        if user_auth_input == "2":
            self.create_account()
        elif user_auth_input == "1":
            self.login()
        else:
            error = colored("please type in one of the options in the menu", "red")
            print(error)
