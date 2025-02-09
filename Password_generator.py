#random.choice(x)= gives a random item from a list
#random.shuffle(x)= to mixed up a list
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME to the pyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

password_list = []

for char in range(1, nr_letters + 1):   
    #password += random.choice(letters)
    password_list.append(random.choice(letters))
    
for char in range(1, nr_symbols + 1):
    #password += random.choice(symbols)
    password_list.append(random.choice(symbols))
    
for char in range(1, nr_numbers + 1):
    #password += random.choice (numbers)
    password_list.append(random.choice(numbers))
    
print(f"Your password is: {password_list}")    
    
random.shuffle(password_list)

print(f"Your password is: {password_list}")

password = ""

for char in password_list:
    password += char
print(f"Your password is: {password}")