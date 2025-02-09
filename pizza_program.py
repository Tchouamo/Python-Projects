print("Welcome to my pizza shop")
print("Here are the prices:")

print("Extra large pizza(20$)")
print("Meduim large pizza(15$)")
print("Small large pizza(10$)")

pizza=input("What pizza size do you want ?(E/M/S)")

bill=0

if pizza == "E":
    option1=input("Do you want peperony with it ?(Y/N) It will make an extra 5$: ")
    option2=input("Will you like a drink with it ?(Y/N) It will make an extra of 7$: ")
    if option1=="Y":
        bill= 20+5
        if option2=="Y":
            bill= 25+7
        else:
            bill= 25
    else:
        bill= 20
        if option2=="Y":
            bill= 20+7
        else:
            bill= 20

elif pizza=="M":
    option1=input("Do you want peperony with it ?(Y/N) It will make an extra 5$: ")
    option2=input("Will you like a drink with it ?(Y/N) It will make an extra of 7$: ")
    if option1=="Y":
        bill= 15+5
        if option2=="Y":
            bill= 20+7
        else:
            bill= 20
    else:
        bill= 15
        if option2=="Y":
            bill= 15+7
        else:
            bill= 15
else:
    option1=input("Do you want peperony with it ?(Y/N) It will make an extra 5$: ")
    option2=input("Will you like a drink with it ?(Y/N) It will make an extra of 7$: ")
    if option1=="Y":
        bill= 10+5
        if option2=="Y":
            bill= 15+7
        else:
            bill= 25
    else:
        bill= 10
        if option2=="Y":
            bill= 10+7
        else:
            bill= 10
            
print(f"Your total bill is {bill}$")
    
