# Password Complexity Checker

# Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.


import re
import random

suggested_passwords = [
    "StrongPass1!",
    "Secure#2024",
    "My$ecret123",
    "P@ssw0rd!",
    "Adm1n$afe!",
]

print("Here are some examples of strong passwords:")
for sp in suggested_passwords:
    print(f" -> {sp}")


while True:
    password = input("Enter a password to assess (or type 'exit' to quit): ")

    if password.lower() == 'exit':
        print("Exiting the program.")
        break

    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    
    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    
    print(f"Password strength: {strength}")
    if not length_criteria:
        print("- Your password should be at least 8 characters long.")
    if not lowercase_criteria:
        print("- Your password should include at least one lowercase letter.")
    if not uppercase_criteria:
        print("- Your password should include at least one uppercase letter.")
    if not number_criteria:
        print("- Your password should include at least one number.")
    if not special_char_criteria:
        print("- Your password should include at least one special character (e.g., @, $, !, %, *, ?, &).")

    print("\n")
