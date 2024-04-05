from get_guess_fn import get_guess                 #
from is_game_over_fn import is_game_over           #
from modules import print_in_color                 #
from print_guess_fn import print_guess             #
####################################################
secret_word=input("Enter the secret word: \n")
guess=input("Enter your guess: \n")
tries_left=5
for i in range(6):
  f_value=is_game_over(secret_word,guess,tries_left)
  if f_value==True:
    break
  else:
    required_letters=print_guess(secret_word,guess)
    print("")
    guess=get_guess(required_letters)
    tries_left-=1