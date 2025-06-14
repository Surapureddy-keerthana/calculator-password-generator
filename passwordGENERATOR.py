import random
import string
def generate_password(length):
    if length<4:
        print("password should contain atleast 4 characters ")
        return ""
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(all_chars, k=length-4)
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    try:
        user_length = int(input("Enter password length: "))
        password = generate_password(user_length)
        if password:
            print("Generated Password:", password)
    except ValueError:
            print("please enter valid number")
        


