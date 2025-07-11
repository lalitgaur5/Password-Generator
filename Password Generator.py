import random
import string

len = int(input("Password length : "))
pass_len = len
CharValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(CharValues)

print("Your Random Password is:", password)