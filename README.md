# Password Strength Checker

A Python program that evaluates the strength of a password and gives clear feedback on how to improve it.

## Features

- Checks password length (8+ characters, 12+ is better)
- Checks for uppercase and lowercase letters
- Checks for numbers and special characters
- Detects common weak patterns like `password` or `123456`
- Classifies passwords as **Weak**, **Medium**, or **Strong**
- Gives specific suggestions to improve security

## How to Run

1. Make sure Python 3 is installed.
2. Run the program:
   ```
   python password_checker.py
   ```
3. Enter a password when prompted. Type `q` to quit.

## Example

```
Enter a password: hello
Password Strength: Weak
Suggestions to improve:
  - Password is too short. Use at least 8 characters.
  - Add at least one uppercase letter (A-Z).
  - Add at least one number (0-9).
  - Add at least one special character (e.g. !@#$%).
```

## How Scoring Works

Each check adds points: length (up to 2), uppercase, lowercase, digit, and special character (1 each). Common weak words subtract 2 points. The final score decides the rating:

| Score | Strength |
|-------|----------|
| 0-2   | Weak     |
| 3-4   | Medium   |
| 5-6   | Strong   |

## Author

Pron1302
