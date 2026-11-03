
def is_armstrong(number):
    if number < 0:
        return False

    digits = len(str(number))
    total = sum(int(digit) ** digits for digit in str(number))

    return total == number
