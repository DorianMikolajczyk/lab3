import string
import random

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(1,8):
        password += random.choice(characters)

    return password

print(generate_password())

