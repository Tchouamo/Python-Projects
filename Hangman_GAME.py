import random  
import hangman_art

print(hangman_art.logo)

world_list=["advark", "baboon", "camel", "clothes", "sexy"]   
choosen_word = random.choice(world_list)
length = len(choosen_word)

#number of lives at the begining of the game
lives = 6

display=[]
#for n in choosen_word:
for n in range(len(choosen_word)):
    display+="_"
print(display)

end_of_game = False
 
while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(length): 
        char = choosen_word[position]
        if char == guess:
            display[position]=char      
    if guess not in choosen_word:
        lives-=1
        print(hangman_art.stages[lives])
    
    print(display)
    print(f"Lives left is {lives}")

    
    if "_" not in display:
        end_of_game=True
        print("congrate for clearing the game") 
