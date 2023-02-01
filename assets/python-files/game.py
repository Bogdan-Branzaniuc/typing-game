import colorama
from colorama import Fore 
from termcolor import colored, cprint 

class Game:
    """
    Handles the menu interfaces of the game and database updates 
    """
    def __init__(self, users_progress_db, typing_state_class):
        self.users_progress_db = users_progress_db
        self.typing_state = typing_state_class()
        self.connected_user = ''

        
    def view_personal_best(self):
        """
        will display the user's Dashboard 
        runs home_menu after displaying the user's progress 
        """
        user_index = self.users_progress_db.col_values(1).index(self.connected_user)
        user_row_num = user_index + 1
        user_row = self.users_progress_db.row_values(user_index + 1)
        print('\n')
        if len(user_row) < 5:
            print(colored(f'Hi {self.connected_user}! you do not have a record yet, start a game first', 'yellow', attrs=['reverse', 'blink']))
        else:
            print(colored('Your personal best is:', 'yellow', attrs=['reverse', 'blink']))
            print('mistakes:', colored(f'{user_row[1]}','green'))
            print('time:', colored(f'{user_row[2]}','green'), 'seconds')
            print('typed characters:', colored(f'{user_row[3]}','green'), 'VS typeable characters:', colored(f'{user_row[4]}','green'))
        print('\n')

           
    def set_user_personal_best(self):
        """
        sets the user mistakes, time and words per minute (a word = 5 chars) in the user_database
        displays this informations to the user when a typing exercise is finished with a message 
        - new personal best if it is the case,  
        """
        user_index = self.users_progress_db.col_values(1).index(self.connected_user)
        user_row_num = user_index + 1
        user_row = self.users_progress_db.row_values(user_index + 1)

        if len(user_row)< 5:
            self.users_progress_db.update(f'B{user_row_num}', self.typing_state.mistakes)
            self.users_progress_db.update(f'C{user_row_num}', self.typing_state.time)
            self.users_progress_db.update(f'E{user_row_num}', self.typing_state.typed_characters)
            self.users_progress_db.update(f'D{user_row_num}', self.typing_state.typeable_characters)
            print('\n\n')
            print(f'{self.typing_state.mistakes} mistakes')
            print(f'{self.typing_state.time} seconds')
            print(f'typeable characters: {self.typing_state.typeable_characters} ')
            print(f'typed characters: {self.typing_state.typed_characters} ')
            print('\n\n')
        else:
            print('\n\n')
            print(f'{self.typing_state.mistakes} mistakes')
            print(f'{self.typing_state.time} seconds')
            print(f'typeable characters: {self.typing_state.typeable_characters} ')
            print(f'typed characters: {self.typing_state.typed_characters} ')

            if self.typing_state.mistakes < int(user_row[1]):
                self.users_progress_db.update(f'B{user_row_num}', self.typing_state.mistakes)
                print(colored(f'Great! new personal best on mistakes', 'green', attrs=['reverse', 'blink']))
            if self.typing_state.time < float(user_row[2]):
                self.users_progress_db.update(f'C{user_row_num}', self.typing_state.time)
                print(colored(f'Great! new personal best on time', 'green', attrs=['reverse', 'blink']))
            if self.typing_state.typed_characters < int(user_row[3]):
                print(colored(f'Great! new personal best on typed characters', 'green', attrs=['reverse', 'blink']))
                self.users_progress_db.update(f'E{user_row_num}', self.typing_state.typed_characters)
                
            self.users_progress_db.update(f'D{user_row_num}', self.typing_state.typeable_characters)
            print('\n\n')

                 
    def home_menu(self):
        """
        Brings up a home menu with 3 options: 
        Start typing
        View your progress
        Log Out
        """
        print(colored('Home menu:', 'blue', attrs=['reverse']))
        print("1. Start typing") 
        print("2. View your progress") 
        print("3. Log Out")
        
        user_home_menu_choice =input(colored('Type in one of the above options:', 'yellow'))
        if user_home_menu_choice == '1':
            self.choose_file_to_type()
        elif user_home_menu_choice == '2':
            self.view_personal_best()
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
        print('\n\n')
        print("1. Rocket launch JS")  
        
        user_choice = input(colored('choose a file to train on by typing the number:', 'yellow'))
        if user_choice == '1':
            file_name='./assets/documents_to_type_on/rocket_js_code.txt'
            self.typing_state.file_name = file_name
            self.typing_state.game_start()
            self.set_user_personal_best()
            
        else:
            ERROR = colored('please type in one of the options in the menu', 'red', attrs=['reverse', 'blink'])
            print(ERROR)