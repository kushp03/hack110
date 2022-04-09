import random
import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
)


pygame.init()

# Other Details
player_score: int = 0

# Set up the drawing window
screen = pygame.display.set_mode([900, 900])

display_surface = pygame.display.set_mode((900, 900))

# pygame clock object controls tick rate
clock = pygame.time.Clock()

# General size and fall speed of all objects:
object_size: int = 25
fall_speed: int = 5

# Setting up objects
object1: pygame.Rect = pygame.Rect(random.randrange(10, 890), -100, object_size * 2, object_size * 2)
object2: pygame.Rect = pygame.Rect(random.randrange(10, 890), 10, object_size * 2, object_size * 2)
object3: pygame.Rect = pygame.Rect(random.randrange(10, 890), -250, object_size * 2, object_size * 2)
object4: pygame.Rect = pygame.Rect(random.randrange(10, 890), -450, object_size * 2, object_size * 2)
object5: pygame.Rect = pygame.Rect(random.randrange(10, 890), -600, object_size * 2, object_size * 2)

# Set up the main character
main_char: pygame.Rect = pygame.Rect(500, 860, 30, 30)
step: int = 20

running: bool = True
collsion: bool = False

while running:

    # BREAK ---------------------------- INITIAL PARAMETERS ----------------------------

    clock.tick(60)

    # Fill background
    screen.fill((120, 200, 255))

    pygame.draw.rect(screen, (150, 150, 150), main_char)

    # Creation of objects 1-5
    pygame.draw.circle(screen, (0, 226, 168), (object1.centerx, object1.centery), object_size)  # Color is light green
    pygame.draw.circle(screen, (246, 90, 168), (object2.centerx, object2.centery), object_size)  # Color is pink
    pygame.draw.circle(screen, (255, 0, 0), (object3.centerx, object3.centery), object_size)  # Color is red
    pygame.draw.circle(screen, (160, 59, 255), (object4.centerx, object4.centery), object_size)  # Color is purple
    pygame.draw.circle(screen, (0, 0, 1), (object5.centerx, object5.centery), object_size)  # Color is black

    # Draws player score on the screen
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(f'Player Score: {player_score}', True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (800, 100)
    screen.blit(text, textRect)
    
    # BREAK ---------------------------- OBJECT ACTIONS FOR OBJECTS 1-5 ----------------------------

    object1.centery += fall_speed  # Cause object #1 to fall
    if object1.centery >= 890:  # If object #1 hits the bottom of the screen, reset its y-parameter.
        object1.centery = 10
        object1.centerx = random.randrange(10, 890)  # Starts the object at some random value of x.
        player_score += 10

    object2.centery += fall_speed  # Cause object #1 to fall
    if object2.centery >= 890:  # If object #1 hits the bottom of the screen, reset its y-parameter.
        object2.centery = 10
        object2.centerx = random.randrange(10, 890)  # Starts the object at some random value of x.
        player_score += 10

    object3.centery += fall_speed  # Cause object #1 to fall
    if object3.centery >= 890:  # If object #1 hits the bottom of the screen, reset its y-parameter.
        object3.centery = 10
        object3.centerx = random.randrange(10, 890)  # Starts the object at some random value of x.
        player_score += 10

    object4.centery += fall_speed  # Cause object #1 to fall
    if object4.centery >= 890:  # If object #1 hits the bottom of the screen, reset its y-parameter.
        object4.centery = 10
        object4.centerx = random.randrange(10, 890)  # Starts the object at some random value of x.
        player_score += 10

    object5.centery += fall_speed  # Cause object #1 to fall
    if object5.centery >= 890:  # If object #1 hits the bottom of the screen, reset its y-parameter.
        object5.centery = 10
        object5.centerx = random.randrange(10, 890)  # Starts the object at some random value of x.
        player_score += 10    

    # IMPORTANT NOTES - It would be cool to increase the size of the object each time it went all the way down so that we can make the game harder.

    # BREAK ---------------------------- OCCURANCES OF KEY PRESS ----------------------------

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                main_char.x += step

            if event.key == K_LEFT:
                main_char.x -= step
            
            if event.key == K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False

    # BREAK ---------------------------- IN THE CASE OF COLLISION ----------------------------
    # Turn Running to false, turn collsion to True
    hit1 = object1.colliderect(main_char)
    hit2 = object2.colliderect(main_char)
    hit3 = object3.colliderect(main_char)
    hit4 = object4.colliderect(main_char)
    hit5 = object5.colliderect(main_char)

    if(hit1):
        running = False
        collision = True

    if(hit2):
        running = False
        collision = True

    if(hit3):
        running = False
        collision = True

    if(hit4):
        running = False
        collision = True

    if(hit5):
        running = False
        collision = True

    # BREAK ---------------------------- FINAL DETAILS ----------------------------

    pygame.display.flip()


# BREAK ---------------------------- CREATION OF FINAL CONCLUSION SCREEN ----------------------------
    # Create a new screen that summarizes that the player won, and give them their final score.
    # Eventually, figure out a way to allow the player to hit the enter key to start a new round that restarts the entire code and allows them to play again.
    # In the case they start a new round, have a variable that keeps track of the highest score achieved in that play.
    # When the code restarts (or anytime the game is played), give the player options in playing a certain mode - hard mode has really quickly falling boulders.




end_screen = pygame.display.set_mode([900, 900])
display_surface = pygame.display.set_mode((900, 900))

while collision:
    screen.fill((120, 200, 255))

    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render(f'You lost!\nThanks for playing! Come back soon!\nYour score was: {player_score}\n Press the escape key to exit or close the tab.', True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (500, 500)
    screen.blit(text, textRect)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            
            if event.key == K_ESCAPE:
                collision = False

        if event.type == pygame.QUIT:
            collision = False
    
    
    pygame.display.flip()

pygame.quit()