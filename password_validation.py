import re

def validate_password(password):
    """
    Validate the password according to the following criteria:
    1. Minimum length of 8 characters.
    2. Contains at least one uppercase letter.
    3. Contains at least one lowercase letter.
    4. Contains at least one number.
    5. Contains at least one special character.
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number."
    
    if not re.search(r'[\W_]', password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is valid."

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to validate: ")
    is_valid, message = validate_password(password)
    print(message)
