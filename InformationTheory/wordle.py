"""
wordle.py
Contains a class that simulates the game of Wordle; used for problems 5-7.
Note to students: your code goes in information_theory.py, not this file.
"""

import numpy as np
# Used for formatting
import colorama
from colorama import Fore, Style
colorama.init()

def load_words(filen):
    with open(filen, 'r') as file:
        # Get all 5-letter words
        words = [line.strip() for line in file.readlines() if len(line.strip()) == 5]
    return words

class WordleGame:
    def __init__(self, allowed_fn='allowed_guesses.txt', possible_fn='possible_secret_words.txt'):
        self.allowed_words = load_words(allowed_fn)
        self.possible_words = load_words(possible_fn)
        self.word = None
        self._game_finished = False
        
    def start_game(self, word=None, display=False):
        """
        Initializes a game of Wordle.
        """
        if word is None:
            word = np.random.choice(self.possible_words)
        else:            
            word = word.lower().strip()
            # Validate the word
            if len(word) != 5:
                raise ValueError("Word must be 5 characters long")
            if word not in self.possible_words:
                raise ValueError('Word must be in the list of possible words')
        self.word = word
        self.display = display
        self.guess_ct = 0
        self.guesses_made = []
        self._game_finished = False
    
    def is_finished(self):
        """
        Returns whether the game has been finished.
        """
        return self._game_finished
    
    def make_guess(self, guess):
        """
        Make a guess for a currently-running game of Wordle
        
        Returns the result of the guess and the total number of guesses made so far.
        
        Arguments:
            guess (str) - a five-letter word that is the guess being made. Must be one of the allowed guesses.
        Returns:
            (tuple of int) - result of the guess. 0 indicates incorrect letter, 1 indicates correct letter in the wrong location, 2 indicates correct letter.
            (int) - number of guesses made so far
        """
        if self.is_finished():
            return self.guess_ct
        elif self.word is None:
            raise ValueError("A game must be started before making a guess")
        guess = guess.lower().strip()
        # Validate the guess
        if len(guess) != 5:
            raise ValueError("Guess must be 5 characters long")
        if guess not in self.allowed_words:
            raise ValueError('Guess must be in the list of allowed words')
        
        # -------
        # Get the result
        result = [0]*5
        l_word = list(self.word)
        l_guess = list(guess)
        for i in range(5):
            if l_word[i] == l_guess[i]:
                result[i] = 2
                l_word[i] = ' '
                l_guess[i] = ' '
        # Check the remaining letters
        for i, c in enumerate(l_guess):
            if c == ' ':
                continue
            if l_word.count(c) > 0:
                # Then the letter exists and is in the wrong place
                t_idx = l_word.index(c)
                result[i] = 1
                l_word[t_idx] = ' '
        result = tuple(result)
        correct = np.all(np.array(result) == 2)        
        
        # Increment guess count
        self.guess_ct += 1
        self.guesses_made.append(guess)
        
        # Output things, complete with color
        if self.display:
            output_chars = (' ', '-', '+')
            output_colors = (Style.RESET_ALL + Fore.WHITE + Style.DIM,
                            Style.RESET_ALL + Fore.YELLOW + Style.NORMAL,
                            Style.RESET_ALL + Fore.GREEN + Style.BRIGHT)
            top_str = ""
            mid_str = ""
            for r, char in zip(result, guess):
                top_str += output_colors[r] + 3*output_chars[r]
                mid_str += output_colors[r] + output_chars[r] + char + output_chars[r]
            print(top_str)
            print(mid_str)
            print(top_str+Style.RESET_ALL)
            if correct:
                print("Congratulations!")
                print("Number of guesses:", self.guess_ct)
        
        if correct:
            self._game_finished = True
            
        return result, self.guess_ct
            
    def play_game_interactive(self, word=None):
        """
        Starts an interactive game of Wordle in the command line.
        """
        self.start_game(word=word, display=True)
        print("Make a guess")
        
        # Main loop
        while self.word is not None:
            try:
                guess = input("> ")
                self.make_guess(guess)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
        