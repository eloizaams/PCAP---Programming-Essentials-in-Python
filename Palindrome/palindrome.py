def palindrome(text):
  """
  Check if the text is a palindrome.

  param: the text
  return True or False
  """
  text = text.replace(" ", "").lower()
  return text == text[::-1].strip()

text = input("Enter the text: ")
if palindrome(text):
  print("'" + text + "' is a palindrome.")
else:
  print("'" + text + "' is not a palindrome.")
    