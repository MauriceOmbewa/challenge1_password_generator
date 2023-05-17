import random
import string

def generate_password(length=8):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    
    # Make sure password is at least 8 characters long
    if length < 8:
        length = 8
    
    # Initialize password with one character from each category
    password = [random.choice(uppercase_letters),
                random.choice(lowercase_letters),
                random.choice(digits),
                random.choice(symbols)]
    
    # Fill remaining password characters randomly from all categories
    for i in range(length - 4):
        password.append(random.choice(uppercase_letters + lowercase_letters + digits + symbols))
    
    # Shuffle password characters to ensure random order
    random.shuffle(password)
    
    # Convert password list to a string and return it
    return ''.join(password)

# Generate a password and print it to the console
password = generate_password()
print(password)
