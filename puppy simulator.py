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

font = pygame.font.SysFont("comicsans", 30)
pygame.display.set_caption("Super Puppy Simulator")



# Game variables
score = 200
puppy_cost = 100
gray_value = 1
orange_value = 2
draw_gray = False
draw_orange = False


# Animation variables
gray_length = 0
orange_length = 0
gray_speed = 1
orange_speed = .5

opaque_gray_length = 0
opaque_orange_length = 0
opaque_gray_speed = 1
opaque_orange_speed = .5

# Upgrade variables
puppy_amount = 0
puppy_cost = 100
buy_puppy = False


# Draw and define functionality of objects on screen
def draw_task(color, y_coord, button_value, draw, length, speed):
    global score



    if draw and length < 180:
        length += speed
    elif draw and length >= 180:
        draw = False
        length = 0
        score += button_value

    pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 180, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 170, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(button_value), True, white)
    screen.blit(value_text, (20, y_coord - 23))
    return pygame.Rect(10, y_coord - 20, 40, 40), length, draw

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


def Money_Loop(color, y_coord, length, speed, score, amount):
    # Draw semi-transparent progress bar
    bar_surface = pygame.Surface((length, 30), pygame.SRCALPHA)
    bar_surface.fill((*color, 150))  # Alpha-blended color
    screen.blit(bar_surface, (70, y_coord - 15))

    if length < 180:
        length += speed
    elif length >= 180:
        length = 0
        score += amount  # Add passive income

    return length, score



# Game loop
running = True
while running:
    timer.tick(framerate)
    screen.fill(background)

    task1, gray_length, draw_gray = draw_task(gray, 50, gray_value, draw_gray, gray_length, gray_speed)
    task2, orange_length, draw_orange = draw_task(orange, 100, orange_value, draw_orange, orange_length, orange_speed)

    puppy_button = puppy_upgrade(800)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_gray = True
            if task2.collidepoint(event.pos):
                draw_orange = True
            if puppy_button.collidepoint(event.pos):
                buy_puppy = True

    if puppy_amount >= 1 and running:
        opaque_gray_length, score = Money_Loop(gray, 50, opaque_gray_length, opaque_gray_speed, score, puppy_amount)


    # Display score
    display_score = font.render(f"$ {round(score,2)}", True, white)
    screen.blit(display_score, (650, 50))

    pygame.display.flip()

pygame.quit()
