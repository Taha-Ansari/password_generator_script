#!/usr/bin/python
import secrets
import string

# Secure password generator
# NIST password guidelines can be used as requirements: 

# - User-generated passwords should be at least 8 characters in length
# - Machine-generated passwords should be at least 6 characters in length
# - Users should be able to create passwords up to at least 64 characters
# - All ASCII/Unicode characters should be allowed, including emojis and spaces
# - Stored passwords should be hashed and salted, and never truncated
# - Prospective passwords should be compared against password breach databases and rejected if there’s a match
# - Users should be prevented from using sequential (ex. “1234”) or repeated (ex. “aaaa”) characters
# - Knowledge-based authentication (KBA), such as “What was the name of your first pet?”, should not be used
# - Users should be allowed 10 failed password attempts before being locked out of a system or service
# - Passwords should not have hints
# - Complexity requirements should not be used, ex. requiring special characters, numbers, uppercase, etc.
# - Context-specific words, such as the name of the service, the user’s username, etc. should not be permitted

# Taken from: https://stealthbits.com/blog/nist-password-guidelines/#:~:text=Password%20Length%20%26%20Processing&text=NIST%20now%20requires%20that%20all,characters%20as%20a%20maximum%20length.

def generate_password(password_length: int, use_symbols: bool, symbols="+=_-!@#$%^&*()") -> str:
    alphanums = string.ascii_letters + string.digits
    if use_symbols: alphanums += symbols
    password = ''.join(secrets.choice(alphanums) for i in range(password_length))
    return password

def check_password(password: str, check_db=True) -> bool:
    password_length = len(password)
    repeat_limit = 3
    count = 1
    
    # Min pass length is 6
    if password_length < 6:
        return False
    
    # Check for repeat characters against a repeat limit (E.g. limit=3 password can't contain 'aaa')
    for current_pos in range(1, password_length):
        if password[current_pos] == password[current_pos-1]:
            count+= 1
        else:
            count = 1
        if count == repeat_limit:
            return False

    # Check for numeric sequences (assuming 0-9 on keyboard and 3+ sequence to match)
    nums = ["123","234","345","456","567","678","789","890"]
    if any(seq in password for seq in nums):
        return False

    # Check for alphabetic sequences (assuming a-z on keyboard and 3+ sequence to match)
    alphabet = string.ascii_letters[:26]
    substr_size = 3
    # Creating list of alphabets divided into 3 per list item
    alpha_list = [alphabet[i:i+substr_size] for i in range(0, len(alphabet))]
    # Getting rid of 'yz', 'z' from the list
    alpha_list = alpha_list[:len(alpha_list) - 2]
    # Check for any matching sequences in alphabet list
    if any(seq in password.lower() for seq in alpha_list):
        return False
    
    if(check_db):
        # Check password with passwords found in common exploit db's (in this case using rockyou as 'db')
        # This isn't the best way to do it, slows down the proccess a lot, prob need to use local db for this search
        with open("rockyou.txt", 'rb') as file:
            for line in file:
                try:
                    word = line.split()[0].decode()
                    if password == word:
                        return False
                except:
                    continue

    # If all checks passed, return true    
    return True

def main():
    pass_length = 8
    password = generate_password(pass_length, False)

    while(not check_password(password, False)):
        print("password failed: " + password)
        password = generate_password(pass_length, False)

    print(password)

if __name__ == '__main__':
    main()