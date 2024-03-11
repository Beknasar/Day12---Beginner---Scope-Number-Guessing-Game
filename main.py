from art import logo
from random import randint

DIFFICULTS = {"easy": 10, "hard": 5}
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def start_init(number):
  print(logo)
  print(f"""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {number}""")

def game_mode():
  """Return attempts number"""
  difficult = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
  return DIFFICULTS[difficult]

def check_attempts(attempts, secret_number):
  """Return """
  if attempts == 0:
    print(f"You've run out of guesses, you lose. The answer was {secret_number}")
    return True
  else:
    return False

def check_guess(guess, secret_number):
  """Return game status win or lose, high or low"""
  if guess != secret_number:
    if guess > secret_number:
      print("Too high")
    else:
      print("Too low")
    print("Guess again")
    return False
  
  else:
    print(f"You got it! The answer was {secret_number}")
    return True

def game():
  is_end = False
  secret_number = randint(0, 100)
  start_init(secret_number)
  attempts = game_mode()
  while not is_end:  
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check = check_guess(guess, secret_number)
    if not check:
      attempts -= 1
      is_end = check_attempts(attempts, secret_number)
    else:
      is_end = check

game()
