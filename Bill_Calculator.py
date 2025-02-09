print("Welcome to the tip Calculator !")
a = int(input("What was the total bill ? $ "))
b = int(input("How much tip would you like to give ? "))
c = int(input("How many people to split the bill ? $ "))
d = (a+b)/c

print(f"Each of you will have to give: {d}$")