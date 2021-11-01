# select random word from words.txt
    # import random module **
    # open txt file using with syntax **
    # put words from txt file into list of strings **
    # select one word from list to use for testing **

# show mystery word as underscores to user **
    # ask for user guess (upper or lowercase does not matter)
    # validate user input if user enters more than one letter
        # show user error: "You can only guess letter a a time. Guess again: "
    
# Show user if guess is part of word **
    # replace underscore with letter **
    # Show letters that have not been guessed
    

# limit number of user guesses to 8
    # keep track of user guess count
    # show user how many guesses are left
    # user only loses guess if guess is incorrect
    # display mystery word if user runs out of guesses
    # show user error if they guess same letter twice. Do not count as a guess in this case.

# Prompt user to play again when the game ends
# Add levels of difficulty based on random word length

import random
words = []
underscores = []
guesses = []
end_game = False

print("Welcome to the mystery word game!! The object of this game is to guess the mystery word before your guesses run out. ")

with open('words.txt') as file:
    strings = file.readlines()

    for string in strings:
        words.append(string)
    # actually get a random word from words.txt
    random_word = words[7].lower()
    random_word = random_word.replace("\n", "")
    print(random_word)

    word_length = range(len(random_word))
    for num in word_length:
        underscores.append('_')
    underscores = "".join(underscores)

    print(underscores)
    user_input = input('Make a guess... ').lower()

    while user_input != 'Quit' and end_game == False:

        for index in range(len(random_word)):
            if random_word[index] == user_input:
                underscores = underscores[0:index] + user_input + underscores[index+1:]
        print(underscores)
        user_input = input('Guess again... ')

        if user_input == 'Quit':
            end_game = True