import pytest
import random
import os,sys
from mock_input_tests import *

from Game import main

def check_if_file_exists():
    try:
        exists = os.path.exists("code_2.py")
        assert exists == True
    except:
        sys.exit()

def test_lower_number():
    random_number = random.randint(1,7)
    guess = random_number+2

    set_keyboard_input([guess,guess-1,guess-2])
    main(random_number)
    output = get_display_output()

    assert output == [
        "\nWelcome to the Guessing Game!",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({guess}) was too high. Try lower.",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({guess-1}) was too high. Try lower.",
        "\nEnter your number guess from one to ten: ",
        f"Hooray!! You guessed the number: ({guess-2}) correctly!"
    ]

def test_higher_number():
    random_number = random.randint(3,10)
    guess = random_number-2

    set_keyboard_input([guess,guess+1,guess+2])
    main(random_number)
    output = get_display_output()

    assert output == [
        "\nWelcome to the Guessing Game!",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({guess}) was too low. Try higher.",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({guess+1}) was too low. Try higher.",
        "\nEnter your number guess from one to ten: ",
        f"Hooray!! You guessed the number: ({guess+2}) correctly!"
    ]

def test_attempts():
    random_number = random.randint(2,9)

    set_keyboard_input([random_number-1,random_number+1,random_number+1])
    main(random_number)
    output = get_display_output()
    assert output == [
        "\nWelcome to the Guessing Game!",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({random_number-1}) was too low. Try higher.",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({random_number+1}) was too high. Try lower.",
        "\nEnter your number guess from one to ten: ",
        f"Your number guess of ({random_number+1}) was too high. Try lower.",
        f"You failed to guess the number ({random_number}) in three attempts."

    ]    