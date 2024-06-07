import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the desired length of each password: "))
        if num_passwords <= 0 or password_length <= 0:
            raise ValueError("Number of passwords and length must be positive integers.")
        
        print("\nGenerating Passwords:")
        for i in range(num_passwords):
            password = generate_password(password_length)
            print(f"Password {i+1}: {password}")
        
        print("\nPasswords generated successfully!")
        print("Remember to store your passwords securely.")
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
