import random
#random module gives us the shuffle function to randomize the card order of the deck list


class WordManager:
    """Class WordManager is responsible for all things pertaining to the guessing word in the game Jumper

    Attributes:
        word_bank (list): holds a list of random words to be used as the word to be guessed
    """
    word_bank = [
        "extract",
        "tissue",
        "ministry",
        "linear",
        "cupboard",
        "diet",
        "film",
        "manner",
        "salvation",
        "biscuit"
    ]

    def get_word(self):
        """Returns a random word from the word_bank list using the random library

        Returns:
            str
        """
        return self.word_bank[random.randint(0, len(self.word_bank))]


