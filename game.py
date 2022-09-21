import simplegui, random
from math import sqrt

center_point = [50, 50] 
window_width = 600 
window_height = 400 
radius = 20 
score = 0 

def draw(canvas):
    canvas.draw_circle(center_point, radius, 1, 'Red', 'Red')    

def timer_handler():
    center_point[0] = random.randint(0, window_height)
	
    center_point[1] = random.randint(0, window_height)    
    
def mouse_handler(pos):    
    global score
    
    dist = sqrt(((pos[0] - center_point[0]) ** 2) + 
                ((pos[1] - center_point[1]) ** 2))
    
    if dist < radius:
        score += 1 
    
	else:
        if score > 0:
            score -= 1 
            
    label.set_text('Score: ' + str(score))

frame = simplegui.create_frame('Click on the ball', window_width, window_height)

timer = simplegui.create_timer(1000, timer_handler)

frame.set_draw_handler(draw)

frame.set_mouseclick_handler(mouse_handler)

label = frame.add_label('Score: ' + str(score))

timer.start() 

frame.start() 
