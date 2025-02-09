import random

choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

comp=str(random.randint(0,3))

if comp=="0" and choice=="0":
    print("The computer picked Rock\nIt's a draw")
if comp=="0" and choice=="1":
    print("The computer picked Rock\nYou won")
if comp=="0" and choice=="2":
    print("The computer picked Rock\nYou lost")

if comp=="1" and choice=="0":
    print("The computer picked Paper\nYou won")
if comp=="1" and choice=="1":
    print("The computer picked Paper\nIt's a draw")
if comp=="1" and choice=="2":
    print("The computer picked Paper\nYou lost")
    
if comp=="2" and choice=="0":
    print("The computer picked Scissors\nYou won")
if comp=="2" and choice=="1":
    print("The computer picked Scissors\nYou lost")
if comp=="2" and choice=="2":
    print("The computer picked Scissors\nIt's a draw")
    
