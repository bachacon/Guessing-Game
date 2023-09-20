### Guessing game w Classes ###

## Original ##
import random

    
class GuessingGame:
    def __init__(self, random_number=None):
        if random_number is None:
            random_number = random.randint(1, 10)
        self.random_number = random_number

    def play_game(self):
        print("\nWelcome to the Guessing Game!")
        correct_guess = False
        for i in range(3):
            user_guess = int(input("\nEnter your number guess from one to ten: "))
            if user_guess > self.random_number:
                print(f"Your number guess of ({user_guess}) was too high. Try lower.")
            elif user_guess < self.random_number:
                print(f"Your number guess of ({user_guess}) was too low. Try higher.")
            else:
                print(f"Hooray!! You guessed the number: ({user_guess}) correctly!")
                correct_guess = True
                break
        if not correct_guess:
            print(f"You failed to guess the number ({self.random_number}) in three attempts.")

def main(random_number=None):
    game = GuessingGame(random_number)
    game.play_game()

if __name__ == "__main__":
    main()

    
            