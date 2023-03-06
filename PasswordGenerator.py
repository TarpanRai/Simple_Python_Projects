# Password generator that you can choose length and complexity

import random
import string


def password_generator(password_length, password_complexity):
    # Get characters to use in password
    lower_case = set(string.ascii_lowercase)
    upper_case = set(string.ascii_uppercase)
    numbers = set(string.digits)
    special_char = set(string.punctuation)
    password = ""

    # Create password of different complexity
    if password_complexity == 1:
        character_sets = [lower_case]
    elif password_complexity == 2:
        character_sets = [lower_case, upper_case]
    elif password_complexity == 3:
        character_sets = [lower_case, upper_case, numbers]
    elif password_complexity == 4:
        character_sets = [lower_case, upper_case, numbers, special_char]
    else:
        character_sets = [lower_case, upper_case, numbers, special_char]

    password = "".join(
        random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(password_length))

    return password


print("-------------------Password Generator--------------------")

# 0.o Trying new technique, didn't know you could do it this way
# Will check if user input is valid
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        complexity = int(input("Enter complexity 1-5: "))
        if complexity < 1 or complexity > 5:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

password = password_generator(length, complexity)
print("Generated Password:", password)

# See how strong the password generated is to brute force attempts
num_characters = len(string.ascii_letters + string.digits + string.punctuation)
attempts_needed = num_characters ** length
print("Number of possible brute force attempts needed:", attempts_needed)
