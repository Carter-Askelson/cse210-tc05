from wordmanager import WordManager


class Director:
    """Director class controls the flow of the Jumper game and manages all dependencies
    
    Attributes:
        user_guesses (list): holds a 2D lists of each letter in the word with a boolean value to determine
        if it was guessed or not.
        user_guesses_left (int): keeps track of how many guesses the user has left
        user_guess_input (str): holds the users input of a guess
        word_manager (obj, WordManager): holds the word bank and randomly gets a new word
        current_word(str): holds the current word picked for the game
    """
    user_guesses_left = 4
    user_guesses = []
    user_guess_input = ""
    word_manager = WordManager()
    current_word = ""

    def start_game(self):
        """this function will start the game and begin game loop

        Returns:
            nothing
        """
        self.current_word = self.word_manager.get_word()
        self.initialize_guesses()

        while self.not_guessed_all_letters() and self.user_guesses_left > 0:
            self.get_word_masked()
            self.display_jumper()
            self.get_user_input()
            self.check_guess()

        if self.user_guesses_left == 0:
            self.get_word_masked()
            self.display_jumper()
            print("\nGAME OVER!")
        else:
            print("\nYOU WIN! GOOD JOB!")


    def get_word_masked(self):
        """Prints the letters of the word if they have been guessed or not

        Returns:
            Nothing
        """
        for element in self.user_guesses:
            if element[1]:
                print(element[0], end=" ")
            else:
                print("_", end=" ")

    def missed_guess(self):
        self.user_guesses_left -= 1

    def get_guesses_left(self):
        """gets the guesses left the user has

        Returns:
             int
        """
        return self.user_guesses_left

    def get_word(self):
        """gets the current word of the game

        Returns:
            str
        """
        return self.current_word

    def get_user_input(self):
        """grabs input from the user

        Returns:
            Nothing
        """
        self.user_guess_input = input("Guess a letter [a-z]: ")

    def check_guess(self):
        """checks to see if the user actually guess the letter correctly

        Returns:
            Nothing
        """
        if self.get_word().__contains__(self.user_guess_input):
            for element in self.user_guesses:
                if element[0] == self.user_guess_input:
                    element[1] = True
        else:
            self.missed_guess()

    def initialize_guesses(self):
        """Sets up our user_guesses 2D list to be able to know which letter to show if the user
        has guessed it correctly

        Returns:
            Nothing
        """
        for letter in self.current_word:
            self.user_guesses.append([str(letter), False])

    def not_guessed_all_letters(self):
        """Checks to see if the user has guessed all the letters correctly in the game

        Returns:
            bool
        """
        correct_guess_count = 0

        for element in self.user_guesses:
            if element[1]:
                correct_guess_count += 1

        return correct_guess_count != len(self.user_guesses)

    def display_jumper(self):
        guesses_left = self.get_guesses_left()

        if guesses_left == 4:
            print("\n       ")
            print("   ___   ")
            print("  /___\  ")
            print("  \   /  ")
            print("   \ /   ")
            print("    O    ")
            print("   /|\   ")
            print("   / \   ")
            print("\n")
            print(" ^^^^^^^ \n")

        elif guesses_left == 3:
            print("\n       ")
            print("  /___\  ")
            print("  \   /  ")
            print("   \ /   ")
            print("    O    ")
            print("   /|\   ")
            print("   / \   ")
            print("\n")
            print(" ^^^^^^^ \n")

        elif guesses_left == 2:
            print("\n       ")
            print("  \   /  ")
            print("   \ /   ")
            print("    O    ")
            print("   /|\   ")
            print("   / \   ")
            print("\n")
            print(" ^^^^^^^ \n")

        elif guesses_left == 1:
            print("\n       ")
            print("   \ /   ")
            print("    O    ")
            print("   /|\   ")
            print("   / \   ")
            print("\n")
            print(" ^^^^^^^ \n")

        elif guesses_left == 0:
            print("\n       ")
            print("    x    ")
            print("   /|\   ")
            print("   / \   ")
            print("\n")
            print(" ^^^^^^^ \n")
