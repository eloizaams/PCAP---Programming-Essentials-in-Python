def life_digit(date):
    """Calculates the Life Digit from a given date in YYYYMMDD format."""
    total = sum(int(digit) for digit in date if digit.isdigit())
    while total > 9:
        total = int(str(total)[0]) + int(str(total)[1])
    return total

date = input("Enter your birth date (YYYYMMDD) ")

print("Your Life Digit is ", life_digit(date))