# Write the is_game_over function here.

def is_game_over(secret_word, guess, tries_left):
  pass
  if tries_left == 0:
    print('Game over! The correct word is {}.'.format(secret_word))
    return True
  elif guess.upper() == secret_word.upper():
    print("Correct! You got it in {} tries!".format(6-tries_left))
    return True
  return False