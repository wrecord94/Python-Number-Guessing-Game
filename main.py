# Number Guessing Game
from art import logo
import random


class NumberGuessingGame:
    def __init__(self):
        self.chosen_number = None
        self.lives = None
        self.user_guess = None
        self.easy_level_lives = 10
        self.hard_level_lives = 6

    def get_difficulty(self):
        """Return the number of lives based on user choosing difficulty level"""
        difficulty_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_chosen == "easy":
            return self.easy_level_lives
        if difficulty_chosen == 'hard':
            return self.hard_level_lives
        else:
            print("Invalid difficulty level. Defaulting to 'easy'.")
            return self.easy_level_lives

    def get_user_guess(self):
        """Method to request and return a user's guess"""
        guess = int(input("Make a guess: "))
        return guess

    def check_guess(self, answer):
        """Checks answer against user's guess and returns provides feedback alongside either True if correct
        otherwise False"""
        if self.user_guess == answer:
            print(f"That's correct! The answer was {answer}!!")
            return True
        elif self.user_guess < answer:
            print("Too low.")
            return False
        elif self.user_guess > answer:
            print("Too high")
            return False

    def game_logic(self):
        """Handles Games-play logic"""
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        self.chosen_number = random.randint(1, 100)
        print(f"Pssst, the correct answer is {self.chosen_number}")

        self.lives = self.get_difficulty()

        won = False
        while self.lives > 0 and won == False:
            print(f"You have {self.lives} lives remaining")
            self.user_guess = self.get_user_guess()
            won = self.check_guess(answer=self.chosen_number)
            self.lives -= 1

        if self.lives == 0:
            print("You've run out of guesses, you lose.")


def start_game():
    number_guessing_game = NumberGuessingGame()
    number_guessing_game.game_logic()


if __name__ == '__main__':
    start_game()
