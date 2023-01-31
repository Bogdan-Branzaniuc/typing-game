import colorama
from colorama import Fore 
from termcolor import colored, cprint 

class Game:
    def __init__(self, users_progress_db, typing_state_class):
        self.users_progress_db = users_progress_db
        self.typing_state = typing_state_class()
        self.connected_user= ''
        
    def view_progress(self):
        """
        will display the user's Dashboard 
        runs home_menu after displaying the user's progress 
        """
        print(self.typing_state.mistakes)
        for count, user in enumerate(self.users_progress_db.col_values(1)):
            if user == self.connected_user:
                print(self.users_progress_db.row_values(count+1))
        
                
    def home_menu(self):
        """
        Brings up a home menu with 3 options: 
        Start typing
        View your progress
        Log Out
        """
        print("1. Start typing") 
        print("2. View your progress") 
        print("3. Log Out")
        
        user_home_menu_choice =input('Type in one of the above options:')
        if user_home_menu_choice == '1':
            self.choose_file_to_type()
        elif user_home_menu_choice == '2':
            self.view_progress()
        elif user_home_menu_choice == '3':
            GREEN_MESSAGE = colored('\n\nSuccessfuly logged out', 'green', attrs=['reverse', 'blink']) 
            print(GREEN_MESSAGE)
            return False
        else:
            ERROR = colored('please type in one of the options in the menu', 'red', attrs=['reverse', 'blink'])
            print(ERROR)


    def choose_file_to_type(self):
        """
        displays a menu with the files available to train on 
        """
        print("1. Rocket launch JS") 
        print("2. test version") 
        user_choice = input('choose a file to train on by typing the number:')
        if user_choice == '1':
            file_name='./assets/documents_to_type_on/rocket_js_code.txt'
            self.typing_state.file_name = file_name
            self.typing_state.game_start()
            
            self.view_progress()
            
        elif user_choice == '2':
            file_name='./assets/documents_to_type_on/short_file.txt'
            self.typing_state.file_name = file_name
            self.typing_state.game_start()
            self.view_progress()
        