from is_valid_guess_fn import is_valid_guess

# Write the get_guess function here.
def get_guess(required_letters):
  pass
  while True:
    guess = input("Enter your guess:\n")
    if is_valid_guess(guess, required_letters) == True:
      return guess
    else:
      print("Your guess must contain all yellow and green letters from your previous guesses.")