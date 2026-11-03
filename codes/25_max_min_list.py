def find_max_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum


if __name__ == "__main__":
    numbers = [10, 20, 5, 40, 15]
    print("Maximum:", find_max_min(numbers)[0])
    print("Minimum:", find_max_min(numbers)[1])