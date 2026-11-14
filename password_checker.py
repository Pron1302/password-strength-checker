import string


def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use 12 or more characters for better security.")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. !@#$%).")

    # Common weak patterns
    common = ["password", "123456", "qwerty", "abc123", "letmein", "admin"]
    if any(w in password.lower() for w in common):
        score -= 2
        feedback.append("Avoid common words or sequences like 'password' or '123456'.")

    # Classification (max score = 6)
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


def main():
    print("=== Password Strength Checker ===")
    while True:
        password = input("\nEnter a password (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        if not password:
            print("Password cannot be empty.")
            continue

        strength, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")

        if feedback:
            print("Suggestions to improve:")
            for tip in feedback:
                print(f"  - {tip}")
        else:
            print("Great job! Your password meets all the criteria.")


if __name__ == "__main__":
    main()
