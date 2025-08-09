import random
import string

size = int(input("Enter password length: "))

def make_pass(size):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

final_pass = make_pass(size)
print("Your Password:", final_pass)
