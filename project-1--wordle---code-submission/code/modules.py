### DO NOT MODIFY ###

# function for printing a character in color to the terminal
# Students source code will call this function. `color` can be 'green', 'red', 'yellow'. 
# This function also returns the text to compare correctness. 
def print_in_color(letter, color):
  text = ''
  if color == 'red':
    text = '\u001b[31m' + letter + '\u001b[0m'
  elif color == 'green':
    text = '\u001b[32m' + letter + '\u001b[0m'
  elif color == 'yellow':
    text = '\u001b[33m' + letter + '\u001b[0m'
  else:
    print("Color is not supported")
    return None
  print(text, end="")
  return text

### DO NOT MODIFY ###