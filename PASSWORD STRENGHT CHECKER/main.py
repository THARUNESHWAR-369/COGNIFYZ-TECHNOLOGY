import re

def password_strength(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return "\n[-] Weak: Password must be at least 8 characters long.\n"

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "\n[-] Weak: Password must contain at least one uppercase letter.\n"

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "\n[-] Weak: Password must contain at least one lowercase letter.\n"

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "\n[-] Weak: Password must contain at least one digit.\n"

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "\n[-] Weak: Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).\n"

    # If all checks pass, the password is considered strong
    return "\n[+] Strong: Password meets all criteria.\n"

while True:
    # Get the user's input for a password
    user_password = input("Enter a password: ")

    # Check the password strength
    result = password_strength(user_password)
    
    # If the password is strong, exit the loop
    if "Strong" in result:
        print(result)
        break
    else:
        print(result)
