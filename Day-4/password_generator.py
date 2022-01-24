import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to The Secret Password Generator")
nletters=int(input("How many letters would you like in your password?\n"))
nnumbers=int(input("How many numbers would you like in your password?\n"))
nsymbols=int(input("How many symbols would you like in your password?\n"))
r=0
password=[]
for i in range(0,nletters):
    r=random.randint(0,len(letters)-1)
    password.append(letters[r])
for i in range(0,nnumbers):
    r=random.randint(0,len(numbers)-1)
    password.append(numbers[r])
for i in range(0,nsymbols):
    r=random.randint(0,len(symbols)-1)
    password.append(symbols[r])
random.shuffle(password)
passwordstring=""
for i in password:
    passwordstring=passwordstring+i
print(f"Your Secure password is: {passwordstring}")



