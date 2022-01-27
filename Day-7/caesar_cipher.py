alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo="""
 _______________
< caesar cipher >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----W |
                ||     ||    

"""
print(logo)

def encrypt(plaintext,shift):
    encrypted=""
    for i in plaintext:
        if i in alphabet:
            l=alphabet.index(i)
            l=(l+shift)%26
            encrypted=encrypted+alphabet[l]
        else:
            encrypted=encrypted+i
    print(f"Encrypted text is {encrypted}")
def decrypt(plaintext,shift):
    decrypted=""
    for i in plaintext:
        if i in alphabet:
            l=alphabet.index(i)
            l=l-shift
            decrypted=decrypted+alphabet[l]
        else:
            decrypted=decrypted+i
    print(f"Decrypted text is {decrypted}")
while(True):
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction=="encode":
        text=input("Type your message:\n").lower()
        shift=int(input("Type the shift number:\n"))
        encrypt(text,shift)
    elif direction=="decode":
        text=input("Type your message:\n").lower()
        shift=int(input("Type the shift number:\n"))
        decrypt(text,shift)
    else:
        print("Try Again")
        continue
    yn=input("Enter 'yes' to run again, 'no' to exit\n")
    if(yn=="no"):
        break

