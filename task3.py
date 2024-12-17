import random
import string

def generate_password():
    print("Password Generator")
    
    try:
        
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
            return
        
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        
        all_characters = lower + upper + digits + special

       
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special),
        ]

        
        password += random.choices(all_characters, k=length - 4)

        random.shuffle(password)

        password = ''.join(password)

        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

generate_password()