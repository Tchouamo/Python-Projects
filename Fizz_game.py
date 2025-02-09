n = int(input("What is the limit of the game: "))
for number in range(1,n+1):
    if number % 3 == 0:
        print(f"{number}: FIZZ")
    elif number % 5 == 0:
        print(f"{number}: BUZZ")
    elif number % 3 == 0 and number % 5 == 0:
        print(f"{number}: FIZZBUZZ")
    else:
        print(f"{number}")
    