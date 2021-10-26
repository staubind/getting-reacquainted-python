# in this version of the game, you only get 5 guesses.
# hi vs low, etc

def runGame():
    # set up a random number
    target = 1 # some random number
    guess_count = 5
    while True:
        guess = input(f'{guess_count} guesses left\n Guess a number: ')
        guess_count -= 1
        try:
            if guess_count > 0:
                if int(guess) == target:
                    print('Congratulations! You were correct.')
                    break
                elif int(guess) > target:
                    print('Too high. Guess again.')
                else:
                    print('Too low. Guess again.')
            
        except ValueError:
                print('Not a number. Please try again.')



if __name__=='__main__':
   runGame()