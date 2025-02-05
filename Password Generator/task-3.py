import random
import string

def generate_password(length):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password.extend(random.choice(all_characters) for _ in range(length - 4))
    
    random.shuffle(password)
    
    return ''.join(password)

def main():

    print("===== Secure Password Generator =====")
    
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            
            # Generate and display password
            password = generate_password(length)
            print("\nGenerated Password:", password)
            
            # Ask if user wants to generate another password
            another = input("\nGenerate another password? (yes/no): ").lower()
            if another != 'yes':
                break
        
        except ValueError:
            print("Please enter a valid number for password length.")
    
    print("\nThank you for using the Password Generator!")

# Run the password generator
if __name__ == "__main__":
    main()