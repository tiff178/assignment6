# Imports
import pygame
import math
import random

# Create functions
def draw_cloud(x, y):
    '''This piece of code is the function to draw the clouds that stay consistent through the program
        param x: the value taken in for the smaller part of the ellipse shape of the cloud
        param y: the value taken in for the longer part of the ellipse shape of the cloud'''
    
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

def draw_fence():
    '''This function draws the entire back fence in the field
        This function takes no parameters'''

    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

def draw_boundary_lines():
    '''This function draws all the out of bounds lines in the soccer field and the penalty box is not included
        This function takes no parameters'''
    
    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)

    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

def draw_score_area():
    '''This function draws the entire scoring area of the field including the poles and scoreboard
        This function takes no parameters'''
    
    #score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)

def draw_goal():
    '''This function draws the outline of the goal (not the net)
    This function takes no parameters'''

    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

def draw_lights():
    '''This function draws the lights and light poles on the back sides of the field
        This function takes no parameters'''

    #light pole 1
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])

    #lights (refactored) - left side of image
    pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
    for x in range(90, 190, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
    for x in range(90, 190, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights (refactored) - right side of image 
    pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
    for x in range(570, 670, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
    for x in range(570, 670, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)

def draw_net(x, y, z, n, m):
    '''This function draws only the vertical lines of the middle portion of the goal
        param x: lower bound of the x-axis
        param y: lower bound of the y-axis
        param z: max range of position of the lines
        param n: the increment of x when drawing veritcal lines
        param m: the increment of y when drawing vertical lines'''
    
    for x in range(x, z, n):
        pygame.draw.line(screen, WHITE, [x+n, 140], [y+m, 200], 1)
        y += m

def draw_net2():
    '''This function draws the rest of the net not inpart one. This includes the side panels and horizontal lines in the middle portion
        This function takes no parameters'''
    
    #net part 2 (refactored/shortened code) - whole net of the left side of the goal
    y = 216
    for x in range (324, 338, 2):
        pygame.draw.line(screen, WHITE, [320, 140], [x+2, y-2], 1)
        y -= 2
    
    #net part 3 (refactored/shortened code) - whole net of the right side of the goal
    x = 476
    for y in range(216, 202, -2):
        pygame.draw.line(screen, WHITE, [480, 140], [x-2, y-2], 1)
        x -= 2

    #net part 4 (refactored/shortened code) - horizontal lines of net in middle portion of the goal
    for y in range(144, 176, 4):
        pygame.draw.line(screen, WHITE, [324, y+4], [476, y+4], 1)
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    for y in range(176, 196, 4):
        pygame.draw.line(screen, WHITE, [335, y+4], [465, y+4], 1)

def draw_stands():
    '''This function draws the two stands at the side of teh screen meant for the audience
        This function takes no parameters'''
    
    #stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])

def draw_flag():
    '''This function draws both of the flags at the sides of the field
        This function takes no parameters'''
    
    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 

def daynight(lights_on, day):
    '''This function determines what kind of colors are relevant to the screen based on the time of day
        param lights_on: boolean value that decides whether the side lights should be on or not (default is on)
        param day: boolean value that determines whether the setting is day or night (default is day == true)'''

    if lights_on == True:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day == True:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

# -- Main Code to run Graphics --
# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

# Config
lights_on = True
day = True

daynight(lights_on, day)

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    clouds.append([x, y])

done = False
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
    #stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
    # stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    draw_fence() # Call the function draw_fence

    for c in clouds: # Call the function draw_could to draw clouds for the sky (Light/Dark)
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))   
    
    draw_boundary_lines() # Call the function draw_boundary_lines
        
    draw_score_area() # Call the function draw_score_area 
    
    draw_goal() # Call the function draw_goal
        
    draw_lights() # Call the function draw_lights
    
    # Call the function draw_net - the main net drawing
    draw_net(320, 338, 360, 5, 3)
    draw_net(360, 361, 376, 4, 4)
    draw_net(376, 376, 420, 4, 4)
    pygame.draw.line(screen, WHITE, [424, 140], [423, 200], 1)
    draw_net(424, 423, 436, 4, 4)
    pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
    draw_net(440, 438, 475, 5, 3)
    
    draw_net2() # Call the function draw_net2 - draw the rest of the lines for the net
    
    draw_stands() # Call the function draw_stands

    draw_flag() # Call the function draw_flag

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)
    # DARKNESS

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()