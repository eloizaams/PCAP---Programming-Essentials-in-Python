def cifra_cesar(text,step):
    """
Encrypts a text using the Caesar cipher with a custom shift.

Args:
    text: The text to be encrypted.
    shift: The shift value (1-25).

Returns:
    The encrypted text.
"""
    new_text = ''
    for char in text:
        if char.isalpha() == False:
            new_text += char
            continue
        else:
            first_position = ord('a') if char.islower() else ord('A')
            ascii = (ord(char) - first_position + step) % 26 + first_position
            new_text += chr(ascii)
    return new_text
    

def get_step():
    """
    Gets a valid shift value from the user.

    Returns:
    An integer representing the shift value (1-25).
    """

    while True:
        try:
            step = int(input("Enter a number between 1..25 to be the step: "))
            if 1 <= step <= 25:
                return step
            else:
                print("Invalid value. The shift must be between 1 and 25.")
        except ValueError:
                print("Invalid input. Please enter an integer.")


print("Cifra text:", cifra_cesar(input("Enter de text: "),get_step()))               