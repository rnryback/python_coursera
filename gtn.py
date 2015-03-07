# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random, simplegui, math

canvas_width=100
canvas_height=200
control_width=200
object_width=150

numb_low=0
numb_high=100
numb=0

guess_rem=0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global numb, guess_rem
    numb=random.randrange(numb_low, numb_high)
    guess_rem=int(math.ceil(math.log(numb_high-numb_low+1,2)))
    print ''
    print 'Let us get started, guess the number between [',numb_low,',',numb_high,').'
    print ' Try to do it in ',guess_rem,' guesses.'


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global numb_low, numb_high
    numb_low=0
    numb_high=100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global numb_low, numb_high
    numb_low=0
    numb_high=1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_rem
    guess_rem -= 1
    guess_numb=int(guess)
    
    print 'Your guess is: ', guess_numb,'.',
    
    
    if guess_numb==numb:
        print 'Nailed it!'
        new_game()
    elif guess_numb>numb:
        print 'Aim lower'
        print 'You still have ',guess_rem, 'guesses.',
    else:
        print ' Aim higher'
        print 'You still have ',guess_rem, 'guesses.',
    if guess_rem<=0:
        print 'No guesses left! Try again?'
        new_game()
# create frame
frame=simplegui.create_frame('Guess the number', canvas_width, canvas_height, control_width)


# register event handlers for control elements and start frame
frame.add_button('Range: 0-100', range100, object_width)
frame.add_button('Range: 0-1000', range1000, object_width)
frame.add_input ('Type your guess down:', input_guess, object_width)
# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
