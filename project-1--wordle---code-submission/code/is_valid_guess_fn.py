# Write the is_valid_guess function here.
def is_valid_guess(guess, required_letters):
  pass
  for char in required_letters:
    if char not in guess:
      return False
  return True