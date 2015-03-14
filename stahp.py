# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
count = 0
tim_check = False
attempts = 0
score = 0
tenth_second = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenth_second
    min = t//600
    temp = (t//10)%60
    sec = temp//10
    ten_sec = temp % 10
    tenth_second = t % 10
    return str(min)+':'+str(sec)+str(ten_sec)+'.'+str(tenth_second)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global tim_check
    timer.start()
    tim_check = True
    
def stop_handler():
    global tim_check,score,attempts,tenth_second
    timer.stop()

    if (tim_check == True) and (tenth_second%10 == 0):
        score +=1
        attempts +=1
    
    elif (tim_check == True):
        attempts +=1
    
    else: tim_check = False

def reset_handler():
    global count,tim_check,score,attempts
    count = 0
    score = 0
    attempts = 0
    tim_check = False
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1
    
# define draw handler
def draw_handler(canvas):
    global count,score,attempts
    canvas.draw_text(format(count),(50,100),50,'Orange')
    canvas.draw_text((str(score)+'/'+str(attempts)),(170,30),18,'White')
    
# create frame
frame=simplegui.create_frame('Stopwatch', 200,200)

# register event handlers
timer=simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start=frame.add_button('Start/Resume!',start_handler,100)
stop=frame.add_button('Stop it!',stop_handler,100)
reset=frame.add_button('Reset it!',reset_handler,100)
# start frame
frame.start()

# Please remember to review the grading rubric
