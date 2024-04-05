# Write the print_guess function here.
from modules import print_in_color
### DO NOT MODIFY ABOVE


def print_guess(secret_word, guess):
  secret_word = secret_word.upper()
  guess = guess.upper()
  required_letters = []
  for index in range(0, len(guess)):
    shoud_print_first_letter_green = secret_word[index] == guess[index] 
    shoud_print_first_letter_red = secret_word[index] != guess[index] 
    if shoud_print_first_letter_green:
      print_in_color(guess[index], 'green')
      required_letters.append(guess[index])
    elif shoud_print_first_letter_red: 
      if guess[index] in secret_word:
        print_in_color(guess[index], 'yellow')
        required_letters.append(guess[index])
      else:
        print_in_color(guess[index], 'red')
  return required_letters
  