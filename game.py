import colorama
from colorama import Fore
from termcolor import colored, cprint
import os
import time


class Game:
    """
    Handles the menu interfaces of the game and database updates
    """

    def __init__(self, users_progress_db, typing_state_class):
        self.users_progress_db = users_progress_db
        self.typing_state = typing_state_class()
        self.connected_user = ""

    def view_personal_best(self):
        """
        will display the user's Dashboard
        runs home_menu after displaying the user's progress
        """
        user_index = self.users_progress_db.col_values(1).index(self.connected_user)
        user_row_num = user_index + 1
        user_row = self.users_progress_db.row_values(user_index + 1)
        os.system('clear')
        
        if len(user_row) < 5:
            no_record_message = f"Hi {self.connected_user}! you do not have a record yet, start a game first"
            print(colored(no_record_message, "yellow"))
        else: 
            print(colored("Your personal best is:", "yellow"))
            print("mistakes:", colored(f"{user_row[1]}", "green"))
            print("time:", colored(f"{user_row[2]}", "green"), "seconds")
            print(
                "typed characters:",
                colored(f"{user_row[4]}", "green"),
                "VS typeable characters:",
                colored(f"{user_row[3]}", "green"),
            )


    def print_user_results(self):
        """
        prints the user results, it get's called only in the set_user_personal_best, after the game-session has ended
        """
        print(colored('Exercise complete. Congrats!','yellow'))
        print(f"{self.typing_state.mistakes} mistakes")
        print(f"{self.typing_state.time} seconds")
        print(f"typeable characters: {self.typing_state.typeable_characters} ")
        print(f"typed characters: {self.typing_state.typed_characters} ")


    def set_user_personal_best(self):
        """
        sets the user result in the user_database if there was no record before
        displays this informations to the user when a typing exercise is finished with a message
        new personal best message is displayed if it is the case for each of the first three values:
        typed characters, time, nr. of mistakes
        """
        os.system('clear')
        user_index = self.users_progress_db.col_values(1).index(self.connected_user)
        user_row_num = user_index + 1
        user_row = self.users_progress_db.row_values(user_index + 1)

        if len(user_row) < 5:
            self.users_progress_db.update(
                f"B{user_row_num}", self.typing_state.mistakes
            )
            self.users_progress_db.update(f"C{user_row_num}", self.typing_state.time)
            self.users_progress_db.update(
                f"E{user_row_num}", self.typing_state.typed_characters
            )
            self.users_progress_db.update(
                f"D{user_row_num}", self.typing_state.typeable_characters
            )
            self.print_user_results()
        else:
            self.print_user_results()

            if self.typing_state.mistakes < int(user_row[1]):
                self.users_progress_db.update(
                    f"B{user_row_num}", self.typing_state.mistakes
                )
                print(colored(f"Great! new personal best on mistakes", "green"))
            if self.typing_state.time < float(user_row[2]):
                self.users_progress_db.update(
                    f"C{user_row_num}", self.typing_state.time
                )
                print(colored(f"Great! new personal best on time", "green"))
            if self.typing_state.typed_characters < int(user_row[3]):
                print(colored(f"Great! new personal best on typed characters", "green"))
                self.users_progress_db.update(
                    f"E{user_row_num}", self.typing_state.typed_characters
                )
            self.users_progress_db.update(
                f"D{user_row_num}", self.typing_state.typeable_characters
            )
            print("\n\n")

    def home_menu(self):
        """
        Brings up a home menu with 3 options:
        Start typing
        View your progress
        Log Out
        """
        title = '''
  ___ ___                            _____                       
 /   |   \  ____   _____   ____     /     \   ____   ____  __ __ 
/    ~    \/  _ \ /     \_/ __ \   /  \ /  \_/ __ \ /    \|  |  \ 
\    Y    (  <_> )  Y Y  \  ___/  /    Y    \  ___/|   |  \  |  /
 \___|_  / \____/|__|_|  /\___  > \____|__  /\___  >___|  /____/ 
       \/              \/     \/          \/     \/     \/       
        '''
        print("\n")
        print(colored(title, "blue"))
        print("1. Start typing")
        print("2. View your progress")
        print("3. Log Out")

        user_home_menu_choice = input(
            colored("Type in one of the above options:", "yellow")
        )
        if user_home_menu_choice == "1":
            os.system('clear')
            self.choose_file_to_type()
        elif user_home_menu_choice == "2":
            os.system('clear')
            self.view_personal_best()
        elif user_home_menu_choice == "3":
            green_message = colored("\n\nSuccessfuly logged out", "green")
            os.system('clear')
            print(green_message)
            return False
        else:
            error = colored("please type in one of the options in the menu", "red")
            os.system('clear')
            print(error)
            self.home_menu()
            return False

    def choose_file_to_type(self):
        """
        displays a menu with the files available to train on
        """
        title = '''
                __                             .___      
   ____   _____/  |_  _______  ____ _____    __| _/__.__.
  / ___\_/ __ \   __\ \_  __ \/ __ \\__  \  / __ <   |  |
 / /_/  >  ___/|  |    |  | \|  ___/ / __ \/ /_/ |\___  |
 \___  / \___  >__|    |__|   \___  >____  |____ |/ ____|
/_____/      \/                   \/     \/     \/\/     
        '''
        print(colored(title, 'red'))
        print("0. back to the home-menu")
        print("1. Rocket launch JS")
        print('\n',
            colored("Once the game starts you will exit the exercice by pressing: ", 'blue'),
            colored("ESC", "red"),
            '\n',
            colored('or by finishing the exercice', 'blue')
        )

        user_choice = input(colored("choose a file to train on or go back:", "yellow"))
        if user_choice == "1":
            os.system('clear')
            file_name = "./assets/documents_to_type_on/rocket_js_code.txt"
            self.typing_state.file_name = file_name
            self.typing_state.esc_pressed=False
            self.typing_state.game_start()
            if self.typing_state.esc_pressed:
                green_message = colored("you exited the exercice", "yellow")
                print(green_message)
            else:
                self.set_user_personal_best()
                
        elif user_choice == "0":
            os.system('clear')
            return False
            self.home_menu()
        else:
            error = colored("please type in one of the options in the menu", "red")
            os.system('clear')
            print(error)
            self.choose_file_to_type()
