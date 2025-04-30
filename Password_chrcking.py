import re

def check_password_strength(password):
    """Evaluates the strength of a password based on various criteria."""
    length = len(password)
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_numbers = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9\s]', password))

    score = 0
    feedback = "Weak"

    if length >= 8:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_numbers:
        score += 1
    if has_special:
        score += 1

    if score >= 4 and length >= 12:
        feedback = "Strong"
    elif score >= 3 and length >= 8:
        feedback = "Moderate"

    return feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
