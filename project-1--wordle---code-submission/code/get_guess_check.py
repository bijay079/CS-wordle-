### DO NOT MODIFY THIS FILE

import sys
from get_guess_fn import get_guess

if len(sys.argv) > 1:
  print(get_guess(sys.argv[1].split(',')))
else:
  print('Use a input paramater to call, e.g: ' + sys.argv[0] + ' A,B')