def reverse_text(text):
  """
  Reverses the input string.
  
  Parameters:
      text(str):The text to reverse.
  Returns: 
       str: The reversed text.
  """
  try:
    return text[::-1]
  except TypeError:
    return "Error: please provide a string."

def add_numbers(a,b):
  """
  Adds two numbers together.

  Parameters:
   a(int or float): First number 
   b(int or float): Second number

  Returns:
   int or float : The sum
  """
  try:
    return float(a) + float(b)
  except(ValueError, TypeError):
    return "Error: please provide two numbers "
