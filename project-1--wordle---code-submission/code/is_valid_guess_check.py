### DO NOT MODIFY THIS FILE

import sys
from is_valid_guess_fn import is_valid_guess

if len(sys.argv) > 2:
  print(is_valid_guess(sys.argv[1], sys.argv[2].split(',')))
else:
  print('Be sure to pass in two inputs to the function, first is the guess and second is the required letters. Ex: ' + sys.argv[0] + 'WORLD W,O,D')