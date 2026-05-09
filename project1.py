def check_password_strength(password):
    """
    Check password strength based on multiple criteria.
    Returns: "Strong", "Medium", or "Weak"
    """
    
    # Input validation - reject empty or too short passwords
    if not password or len(password) < 8:
        return "Weak"
    
    score = 0

    # 1. Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    # 2. Check for lowercase letters a-z
    if any(c.islower() for c in password):
        score += 1
    
    # 3. Check for uppercase letters A-Z
    if any(c.isupper() for c in password):
        score += 1
    
    # 4. Check for numbers 0-9
    if any(c.isdigit() for c in password):
        score += 1
    
    # 5. Check for special characters (symbols)
    if any(not c.isalnum() for c in password):
        score += 1
    
    # 6. Penalty for consecutive repeating characters
    has_consecutive = any(password[i] == password[i+1] for i in range(len(password)-1))
    if has_consecutive:
        score -= 1
    
    # 7. Return result based on score
    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


def display_result(strength):
    """
    Display password strength result and general recommendations.
    """
    print(f"\nPassword Strength: {strength}")
    
    # General recommendations (without revealing specifics)
    print("\nRecommendations:")
    if strength == "Weak":
        print("  • Use a longer password with a mix of different character types")
        print("  • Avoid common words or patterns")
    elif strength == "Medium":
        print("  • Consider making it longer and adding more variety")
        print("  • Include special characters for better security")
    else:
        print("  • Excellent choice! Keep it secure and unique.")


# Main program
if __name__ == "__main__":
    print("=" * 40)
    print("   PASSWORD STRENGTH CHECKER")
    print("=" * 40)
    
    while True:
        password = input("\nEnter your password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Thank you for using Password Strength Checker!")
            break
        
        if len(password) == 0:
            print("Password cannot be empty!")
            continue
        
        strength = check_password_strength(password)
        display_result(strength)