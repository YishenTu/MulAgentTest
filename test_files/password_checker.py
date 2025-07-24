def check_password_strength(password):
    """
    Check the strength of a password and return a score from 0-100.
    
    Scoring criteria:
    - Length: <6 (weak), 6-10 (medium), >10 (strong)
    - Character types: uppercase, lowercase, numbers, special characters
    
    Args:
        password (str): The password to check
        
    Returns:
        dict: Contains 'score' (0-100), 'strength' level, and 'details'
    """
    if not password:
        return {
            'score': 0,
            'strength': 'weak',
            'details': {
                'length': 0,
                'has_uppercase': False,
                'has_lowercase': False,
                'has_numbers': False,
                'has_special': False
            }
        }
    
    # Initialize score
    score = 0
    
    # Check length and assign base score
    length = len(password)
    if length < 6:
        length_score = 10  # Weak
        strength = 'weak'
    elif 6 <= length <= 10:
        length_score = 30  # Medium
        strength = 'medium'
    else:
        length_score = 50  # Strong
        strength = 'strong'
    
    score += length_score
    
    # Check character types (each type adds points)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    # Add points for each character type present
    if has_uppercase:
        score += 12.5
    if has_lowercase:
        score += 12.5
    if has_numbers:
        score += 12.5
    if has_special:
        score += 12.5
    
    # Determine final strength level based on score
    if score < 40:
        strength = 'weak'
    elif 40 <= score < 70:
        strength = 'medium'
    else:
        strength = 'strong'
    
    return {
        'score': score,
        'strength': strength,
        'details': {
            'length': length,
            'has_uppercase': has_uppercase,
            'has_lowercase': has_lowercase,
            'has_numbers': has_numbers,
            'has_special': has_special
        }
    }


def main():
    """Test the password strength checker with sample passwords."""
    test_passwords = ["abc", "Password1", "MyStr0ng!Pass"]
    
    print("Password Strength Checker")
    print("=" * 50)
    
    for password in test_passwords:
        result = check_password_strength(password)
        
        print(f"\nPassword: {password}")
        print(f"Score: {result['score']}/100")
        print(f"Strength: {result['strength']}")
        print("Details:")
        print(f"  - Length: {result['details']['length']} characters")
        print(f"  - Has uppercase: {result['details']['has_uppercase']}")
        print(f"  - Has lowercase: {result['details']['has_lowercase']}")
        print(f"  - Has numbers: {result['details']['has_numbers']}")
        print(f"  - Has special characters: {result['details']['has_special']}")


if __name__ == "__main__":
    main()