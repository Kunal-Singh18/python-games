import random,string

length=int(input("enter the length of password required:"))

space=string.ascii_letters+string.punctuation+string.digits
password=""
for i in range(length):
    password+=random.choice(space)

print(password)
