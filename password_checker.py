import string

#password = input("Enter your password: ")

def password_checker(password):
    strength = 0
    feedback = ''
    lower_count = upper_count = num_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char in string.punctuation:
            special_count += 1

    if len(password) >= 8:
        strength += 1
    else:
        print("Password should be at least 8 characters long!")

    if lower_count >= 1:
        strength += 1
    else:
        print("Add at least one lowercase letter!")
    if upper_count >= 1:
        strength += 1
    else:
        print("Add at least one uppercase letter!")
    if num_count >= 1:
        strength += 1
    else:
        print("Add at least one number!")
    if special_count >= 1:
        strength += 1
    else:
        print("Add at least one special character!")

    if strength == 5:
        comment = print("Strong Password!")
    elif 3 <= strength < 5:
        comment = print("Moderate Password!")
    else:
        comment = print("Weak password!")

    print(f"\nPassword Strength: {comment}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")
    elif strength == 5:
        print("Great job! Your password meets all security standards!")

if __name__ == "__main__":
 user_password = input("Enter your password: ")
 password_checker(user_password)
