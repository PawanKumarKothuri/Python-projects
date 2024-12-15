import random
import string
import math

def generate_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return "No character types selected!"
    if length < 1:
        return "Password length must be at least 1."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def calculate_entropy(length, pool_size):
    return length * math.log2(pool_size)

def evaluate_strength(entropy):
    if entropy < 28:
        return "Weak"
    elif entropy < 56:
        return "Moderate"
    elif entropy < 70:
        return "Strong"
    else:
        return "Very Strong"

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to passwords.txt!")

# User inputs
length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate password
password = generate_password(length, include_uppercase, include_numbers, include_special)
print(f"Generated Password: {password}")

# Calculate entropy and strength
pool_size = len(string.ascii_lowercase)
if include_uppercase:
    pool_size += len(string.ascii_uppercase)
if include_numbers:
    pool_size += len(string.digits)
if include_special:
    pool_size += len(string.punctuation)

entropy = calculate_entropy(length, pool_size)
strength = evaluate_strength(entropy)
print(f"Entropy: {entropy:.2f} bits - Strength: {strength}")

# Save password
save_option = input("Do you want to save this password? (y/n): ").lower() == 'y'
if save_option:
    save_password(password)
