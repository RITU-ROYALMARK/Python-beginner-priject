#HANGMAN PROJECT FORM PYTHON
import random # import random for get the random choice from the list
# import the hangman design file for hangman picture for another py file
import HANGMAN_DESIGN
#first create a list of character
l = ["apple","mango","jackfruit","orange","graphs","pineapple"]
choice = random.choice(l)# piciking random object form the list
print(choice)

blank = ["_"] *len(choice)

lives = 0
game_over = False

while game_over is not True:
    player = input("enter the character: ")
    for position in range(len(choice)):
        guessed = choice[position]
        if player == guessed:
            blank[position] = player
    print(blank)
    if player not in choice: # check if player input is not there in choice or not and minus one lives
        print(HANGMAN_DESIGN.list[lives])  # its going to print the hangman design
        lives += 1

        if lives > 7:
            game_over = True

            print("YOU LOSSE")
    if "_" not in blank: # check if there is any empty space in blank the game over is true break loop you win
        game_over = True
        print("YOU WIN")
