import pygame
import time
pygame.init()

# Color library
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (127, 0, 127)
orange = (255, 165, 0)
yellow = (255, 255, 0)
dark_green = (46, 139, 87)
gray = (128, 128, 128)
brown = (150, 75, 0)

screen = pygame.display.set_mode((1000, 800))
framerate = 60
background = black
timer = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 30)
pygame.display.set_caption("Super Puppy Simulator")



# Game variables
score = 200
puppy_cost = 100
puppy_value = 1
Spuppy_value = 5
draw_puppy = False
draw_Spuppy = False


# Animation variables
puppy_length = 0
Spuppy_length = 0
puppy_speed = 1
Spuppy_speed = .5

#load sprites
puppy_sprite = pygame.image.load('Puppy.gif')
Spuppy_sprite = pygame.image.load('Strong Puppy.png')

#transform scale
puppy_sprite = pygame.transform.scale(puppy_sprite,(64,64))
Spuppy_sprite = pygame.transform.scale(Spuppy_sprite,(64,64))

#get rectangles surrounding images
puppy_rect = puppy_sprite.get_rect()
Spuppy_rect = Spuppy_sprite.get_rect()

#position sprites
puppy_rect.topleft = (10,20)
Spuppy_rect.topleft = (10,80)

opaque_gray_length = 0
opaque_orange_length = 0
opaque_gray_speed = 1
opaque_orange_speed = .5

# Upgrade variables
puppy_amount = 0
puppy_cost = 100
buy_puppy = False


#makes the score go up smoothly each tick (60 tps)
def smooth_add(score,money):

    while(money > 0):
        score+=1

    # Display score
    display_score = font.render(f"$ {round(score, 2)}", True, white)
    screen.blit(display_score, (650, 50))



# Display and define functionality of objects on screen
def draw_task(color, y_coord, button_money, draw, length, speed):
    global score

    if draw and length < 180:
        length += speed
    elif draw and length >= 180:
        draw = False
        length = 0
        score += button_money

    # display sprites
    screen.blit(puppy_sprite, puppy_rect)
    screen.blit(Spuppy_sprite, Spuppy_rect)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 180, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 170, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    #display text
    value_text = font.render(f"${str(button_money)}", True, white)
    screen.blit(value_text, (23, y_coord - 13))
    return pygame.Rect(10, y_coord - 20, 40, 40), length, draw

# Draw and define functionality of the "puppy" upgrade
def puppy_upgrade(x_coord):
    global puppy_amount, buy_puppy, score, puppy_cost

    # Button box
    puppy = pygame.draw.rect(screen, gray, [x_coord, 340, 150, 100])
    display_cost = font.render(f"${round(puppy_cost, 2)}", True, green)
    screen.blit(display_cost, (x_coord + 35, 290))



    # Buying logic
    if buy_puppy and score >= puppy_cost:
        puppy_amount += 1
        score -= puppy_cost
        buy_puppy = False

    puppy_cost = (100 * (1.15 ** puppy_amount))
    # Display puppy amount
    puppy_amount_text = font.render(f"Puppies: {puppy_amount}", True, white)
    screen.blit(puppy_amount_text, (x_coord + 5, 350))

    return puppy

# a function that adds money to score automatically
def Money_Loop(color, y_coord, length, puppy_speed, score, amount):
    # Draw semi-transparent progress bar
    bar_surface = pygame.Surface((length, 30), pygame.SRCALPHA)
    bar_surface.fill((*color, 150))  # Alpha-blended color
    screen.blit(bar_surface, (70, y_coord - 15))

    if length < 180:
        length += puppy_speed
    elif length >= 180:
        length = 0
        score += amount  # Add passive income

    return length, score



# Game loop
running = True


while running:
    timer.tick(framerate)
    screen.fill(background)

    #load puppy task
    task1, puppy_length, draw_puppy = draw_task(gray, 80, puppy_value, draw_puppy, puppy_length, puppy_speed)

    #load strong puppy task
    task2, Spuppy_length, draw_Spuppy = draw_task(orange, 160, Spuppy_value, draw_Spuppy, Spuppy_length, Spuppy_speed)

    puppy_button = puppy_upgrade(800)


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if puppy_rect.collidepoint(event.pos):
                draw_puppy = True
            if Spuppy_rect.collidepoint(event.pos):
                draw_Spuppy = True
            if puppy_button.collidepoint(event.pos):
                buy_puppy = True


    if puppy_amount >= 1 and running:
        opaque_gray_length, score = Money_Loop(gray, 50, opaque_gray_length, opaque_gray_speed, score, puppy_amount)


    smooth_add(score,)

    # Display mouse coordinates
    if event.type == pygame.MOUSEMOTION:
        mouse_pos = str(pygame.mouse.get_pos())
        mouse_pos = font.render(mouse_pos, True, white)
        screen.blit(mouse_pos, (500, 400))





    pygame.display.flip()

pygame.quit()
