from random import shuffle

#Function to shuffle a list
def shuffled_up(list):
    shuffle(list)
    return list

# Function to take a player guess
def player_guess():
    
    guess = ''

    while guess not in ['0','1','2']:

        guess = input("Please have a guess: 0, 1 or 2 \n")
    
    return int(guess)

# Function to check if guess is correct
def check_guess(list, guess):

    if list[guess] == 'O':
        print("We've got a winner! Lucky little shit")
    else:
        print("Nice try you nerd. How'd you miss it?")
        print(list)

# Logic for the interactions

#Inital list
game = [" ","O"," "]

# Shuffled list
shuffled_game = shuffled_up(game)

# Player guess
guess = player_guess()

#Checking guess
check_guess(shuffled_game,guess)
