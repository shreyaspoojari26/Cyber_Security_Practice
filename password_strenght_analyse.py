import re
import hashlib

print("===== PASSWORD STRENGTH ANALYZER =====")

password = input("Enter your password: ")

score = 0
suggestions = []

# Check length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# Check uppercase
if re.search("[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

# Check lowercase
if re.search("[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

# Check number
if re.search("[0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one number.")

# Check special character
if re.search("[!@#$%^&*]", password):
    score += 1
else:
    suggestions.append("Add a special character.")

# Check common passwords
common_passwords = [
    "password",
    "12345678",
    "qwerty",
    "admin123",
    "password123"
]

if password.lower() in common_passwords:
    score = 1
    suggestions.append("Avoid common passwords.")

# Display strength
print("\nPassword Strength:")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")

# Suggestions
if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password is strong!")

# Hash password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nSHA-256 Hash:")
print(hashed_password)
