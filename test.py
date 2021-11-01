# import random module to populate through the words.txt file to choose a word at random
import random

print("Welcome to the Mystery Word Game!! The object of this game is to guess the random generated word within 8 guesses. You will have three difficulty levels to choose from. Easy will generate a word that has a length between 4-6 characters. Normal will generate a word that has a length between 6-8 characters. Hard will generate a word that is 8 characters or more. Choose wisely!! ")

# setting variables for the different difficulty level word list
Easy = []
Normal = []
Hard = []
# setting a variable to check that the player enter a valid character from the alphabet
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

with open('words.txt') as file:
    strings = file.readlines()
    for string in strings:
        string = string.strip().lower()
        if (3 < len(string) < 7):
            Easy.append(string)
        if (5 < len(string) < 9):    
            Normal.append(string)
        if (7 < len(string)):     
            Hard.append(string)
            
def play_list(words):
    r = random.randint(0,len(words)-1)
    word = words[r]
    guess_count = 8
    guesses = []
    while guess_count > 0:
        guess_word = display_word(word, guesses)
        print(guess_word)
        if "_" not in guess_word:
            print("You win!!!")
            break
        else:
            guess = input("Make a guess: ")
            if (1 == len(guess)): 
                # checking the guess to ensure it is in the alphabet string variable defined at the top
                if guess in alphabet_string:
                    if guess not in guesses:
                        # this next line appends all guesses to the guesses list
                        guesses.append(guess)
                        guess_count = guess_count - 1
                        if guess in word:
                            # if the player guesses a correct letter this next line will print Good guess
                            print("Good guess!")
                        else:
                            # if the player guesses a incorrect letter this will print the below statement
                            print("Opps, that letter is not in your mystery word. Guess again")
                            if guess_count == 0:
                                # if the play runs out of guesses this will print the below comment
                                print("You lost!!")
                    else:
                        print("You have already guessed that letter. Please guess again")
                else:
                    print("You must guess a letter in the alphabet")
            else:
                print("You must only guess one letter")
        

    
# This function creates the display of the mystery word
def display_word(word, guesses):
    # setting the output to a string
    output = ""
    for letter in word:
        if letter in guesses:
            output = output + letter + " "
        else:
            output = output + "_ "
    return output

# this function defines which word list the user will be guessing from depending on the difficulty chosen
def game_loop():
    user_input = input("Please choose a difficulty level of Easy, Normal, or Hard: ")
    user_input = user_input.lower().strip()
    if user_input == "easy":
        play_list(Easy)
    elif user_input == "normal":
        play_list(Normal)
    elif user_input == "hard":
        play_list(Hard)
    else: 
        print("That is not a valid choice") 
        game_loop()
        
        
        
        
game_loop()



