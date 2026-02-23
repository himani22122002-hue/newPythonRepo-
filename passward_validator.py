def password_validator(passward):
    if len(passward)<8:
        return "Password must be at least 8 characters long."
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    for char in passward:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    if not (has_upper and has_lower and has_digit and has_special):
        return "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
    return "Password is valid."
# Example usage
password=input("Enter a password:")
print(password_validator(password))