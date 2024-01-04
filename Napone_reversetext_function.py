def reverse_string():
  while True:
    text = input("Enter a string: ")
    if not text.isalpha():  # Check if all characters are letters
      print("Error Reported! Enter text only.")
    else:
      reversed_text = text[::-1]  # Reverse using slicing
      print("Output:", reversed_text)
      break

reverse_string()
