class Game:
    def __init__(self):
        self.running = True

    def main_menu(self):
        while self.running:
            print("\nWelcome to the Text-Based Game!")
            print("1. Start Game")
            print("2. Load Game")
            print("3. Options")
            print("4. Exit")

            choice = input("Please choose an option (1-4): ")

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
        # Implement game logic here
        self.game_loop()

    def load_game(self):
        print("\nLoading game...")
        # Implement load logic here
        pass

    def show_options(self):
        print("\nGame Options:")
        print("1. Sound: On")
        print("2. Difficulty: Normal")
        print("3. Back to Menu")
        choice = input("Choose an option (1-3): ")
        if choice == '3':
            return
        else:
            print("Option not implemented yet.")

    def exit_game(self):
        print("Thank you for playing!")
        self.running = False

    def game_loop(self):
        while True:
            print("\nYou are in a dark room. What do you want to do?")
            print("1. Look around")
            print("2. Open door")
            print("3. Check inventory")
            print("4. Exit game")
            
            action = input("Choose an action (1-4): ")

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
    game = Game()
    game.main_menu()