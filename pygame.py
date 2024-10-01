import json

class Game:
    def __init__(self, config_file):
        self.running = True
        self.current_room = 'room1'  # Starting room
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
            room = self.config['rooms'][self.current_room]
            print("\n" + room['description'])
            self.display_menu(room)

            action = input("Choose an action: ")

            next_room = None
            for option in room['options']:
                if action == option['key']:
                    if 'next_room' in option:
                        next_room = option['next_room']
                    elif option['text'] == "Look around":
                        print("You observe your surroundings.")
                    elif option['text'] == "Check inventory":
                        print("You have no items in your inventory.")
                    break

            if next_room:
                self.current_room = next_room
            elif action == '4':
                print("Exiting the game...")
                break
            else:
                print("Invalid action. Please try again.")

if __name__ == "__main__":
    game = Game('game_config.json')
    game.main_menu()
