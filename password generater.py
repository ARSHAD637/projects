def password_finder(password):
    # check if password contains at least one uppercase letter, one lowercase letter, one digit and one special character
    if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in '@!%&*' for char in password):
        return password
    else:
        # find the first uppercase letter, first lowercase letter, first digit and first special character in the password
        for char in password:
            if char.isupper():
                return password[:password.index(char)].upper() + password[password.index(char):]
            elif char.islower():
                return password[:password.index(char)].lower() + password[password.index(char):]
            elif char.isdigit():
                return password[:password.index(char)].replace(char, '9') + password[password.index(char):]
            elif char in '@!%&*':
                return password[:password.index(char)].replace(char, '#') + password[password.index(char):]
            
