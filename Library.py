from zxcvbn import zxcvbn

def analyze_password(password):
    """
    Analyze the password using zxcvbn and provide feedback.
    """
    results = zxcvbn(password)
    score = results['score']
    suggestions = results['feedback']['suggestions']
    warning = results['feedback']['warning']

    return score, suggestions, warning

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    score, suggestions, warning = analyze_password(password)
    print(f"Score: {score}")
    print("Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
    if warning:
        print(f"Warning: {warning}")
