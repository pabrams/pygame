import json

class Game:
    def __init__(self, config_file):
        self.running = True
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def display_menu(self, menu):
        print("\n" + menu.get('title', 'Menu'))
        for option in menu.get('options', []):
            print(f"{option['key']}. {option['text']}")
    
    def main_menu(self):
        while self.running:
            self.display_menu(self.config['main_menu'])
            choice = input("Please choose an option: ")

            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.load_game()
            elif choice == '3':
                self.show_options()
            elif choice == '4':
                self.exit_game()
            else:
                print("Invalid choice. Please try again.")

    def start_game(self):
        print("\nStarting a new game...")
        self.game_loop()

    def load_game(self):
        print("\nLoading game...")
        # Implement load logic here
        pass

    def show_options(self):
        self.display_menu(self.config['options_menu'])
        choice = input("Choose an option: ")
        if choice == '3':
            return
        else:
            print("Option not implemented yet.")

    def exit_game(self):
        print("Thank you for playing!")
        self.running = False

    def game_loop(self):
        while True:
            self.display_menu(self.config['game_loop'])
            action = input("Choose an action: ")

            if action == '1':
                print("You see shadows in the corners of the room.")
            elif action == '2':
                print("The door creaks open to reveal a bright hallway.")
            elif action == '3':
                print("You have no items in your inventory.")
            elif action == '4':
                print("Exiting the game...")
                break
            else:
                print("Invalid action. Please try again.")

if __name__ == "__main__":
    game = Game('game_config.json')
    game.main_menu()