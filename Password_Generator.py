import random
import secrets
import string


try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()


letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


all_chars = letters + numbers + symbols

password = [
    secrets.choice(letters),
    secrets.choice(numbers),
    secrets.choice(symbols)
]


for _ in range(length - 3):
    password.append(secrets.choice(all_chars))


secrets.SystemRandom().shuffle(password)


final_password = ''.join(password)
print("Generated password:", final_password)