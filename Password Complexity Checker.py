import re

def check_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search('[^A-Za-z0-9]', password))

    score = 0
    feedback = []

    # Length check
    if length >= 8:
        score += 1
    else:
        feedback.append("8 characters length")

    # Uppercase check
    if has_uppercase:
        score += 1
    else:
        feedback.append(" At least one uppercase letter")

    # Lowercase check
    if has_lowercase:
        score += 1
    else:
        feedback.append("At least one lowercase letter")

    # Digit check
    if has_digit:
        score += 1
    else:
        feedback.append("At least one digit")

    # Special character check
    if has_special:
        score += 1
    else:
        feedback.append("At least one special character")

    # Determine strength and provide specific feedback
    if score == 5:
        strength = "Very Strong"
        feedback_text = "Your password strength is very strong and no one can guess it."
    elif score == 4:
        strength = "Strong"
        feedback_text = f"Your password strength is strong but lacks: {', '.join(feedback)}."
    elif score == 3:
        strength = "Moderate"
        feedback_text = f"Your password strength is moderate and you can make it strong by adding features like: {', '.join(feedback)}."
    elif score == 2:
        strength = "Weak"
        feedback_text = f"Your password strength is weak and you can enhance your password with: {', '.join(feedback)}."
    else:
        strength = "Easy"
        feedback_text = f"Your password is easy and so that everyone could easily guess it. Add some more features to it: {', '.join(feedback)}."

    return strength, feedback_text

# Run the check for five times
for _ in range(5):
    password = input("Enter a password: ")
    strength, feedback = check_password_strength(password)

    print(f"Password Strength: {strength}")
    print("Feedback:")
    print(feedback)