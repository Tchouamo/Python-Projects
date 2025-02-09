#Use .index(x) to get the index of a code
import art
print(art.logo)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p", 
            "q", "r", "s", "t", "u", "v", "w", "x", 
            "y", "z", "a", "b", "c", "d", "e", "f", 
            "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", 
            "w", "x", "y", "z"]

def encrypt(plane_text,move):
    cipher_text=""
    for char in plane_text: 
        position = alphabet.index(char) 
        new_position = position + move
        new_char = alphabet[new_position]   
        cipher_text += new_char
    print(f"The encrypted code is {cipher_text}")
    
def decrypt(cipher_text,move):
    plain_text=""
    for char in cipher_text: 
        position = alphabet.index(char)  
        new_position = position - move     
        new_char = alphabet[new_position]   
        plain_text += new_char
    print(f"The decrypted code is {plain_text}")
    
operation = int(input("What do you want to do ? 1-ENCRYPT OR 2-DECRYPT: "))
message = input("Enter the message: ")
shift = int(input("What is the shift pattern? "))
code=""

if operation ==1:
    encrypt(plane_text=message,move=shift)
    
elif operation ==2:
    decrypt(cipher_text=message,move=shift)
    
else:
    print("Incorrect entry")