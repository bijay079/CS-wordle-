### DO NOT MODIFY THIS FILE
import sys
from print_guess_fn import print_guess

if len(sys.argv) > 1:
  required_letters = print_guess(sys.argv[1], sys.argv[2])
  print("")
else:
  print('Be sure to pass in two inputs to the function, first is the secret_word and the second is your guess.')