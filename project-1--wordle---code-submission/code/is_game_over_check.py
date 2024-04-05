### DO NOT MODIFY THIS FILE
import sys
from is_game_over_fn import is_game_over

if len(sys.argv) > 2:
  game_over = is_game_over(sys.argv[1], sys.argv[2], int(sys.argv[3]))
  print("")
else:
  print('Be sure to pass in three inputs to the function, first is the secret_word and the second is your guess, and the third is tries_left')