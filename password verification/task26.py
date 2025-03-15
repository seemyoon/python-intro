# 1. Create a function to verify the password
# 2. The password must be at least 8 characters long
# 3. The password must contain:
# - Lowercase letters
# - Uppercase letters
# - Numbers
# - Special symbols
# 4. Ask the user to enter the password in the terminal and check it using created function
import re


def verify_password(password):
    password_regexp = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    is_valid = bool(re.match(password_regexp, password))
    return is_valid


while True:
    print("Enter 'quit' in order to exit from login")
    user_input = input("Enter new password in the terminal: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if verify_password(user_input):
        print("Login successfully")
        break
    else:
        print("Your new should match patterns")
