import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=" * 40)
    print("      PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    upper = input("Include Uppercase letters? (y/n): ").lower() == "y"
    lower = input("Include Lowercase letters? (y/n): ").lower() == "y"
    numbers = input("Include Numbers? (y/n): ").lower() == "y"
    symbols = input("Include Symbols? (y/n): ").lower() == "y"

    password = generate_password(length, upper, lower, numbers, symbols)

    if password:
        print("\nGenerated Password:")
        print(password)
    else:
        print("Error: Select at least one character type.")


if __name__ == "__main__":
    main()