import re
from zxcvbn import zxcvbn

def detailed_password_feedback(password):
    """
    Validate the password and provide detailed feedback.
    """
    feedback = []

    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")

    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")

    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")

    if not re.search(r'[\W_]', password):
        feedback.append("Password should contain at least one special character.")

    # Using zxcvbn to provide more advanced feedback
    results = zxcvbn(password)
    score = results['score']
    suggestions = results['feedback']['suggestions']

    # Mapping score to a friendly message
    score_message = {
        0: "Password is very weak.",
        1: "Password is weak.",
        2: "Password is fair.",
        3: "Password is good.",
        4: "Password is strong."
    }

    feedback.append(score_message[score])
    feedback.extend(suggestions)

    if not feedback:
        feedback.append("Password is valid and strong.")
    
    return feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to validate: ")
    feedback = detailed_password_feedback(password)
    for message in feedback:
        print(message)
