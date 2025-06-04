import pygame
pygame.init()

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
orange = (255, 165, 0)

# Screen and fonts
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Super Puppy Simulator")
font = pygame.font.SysFont("bahnschrift", 30)
clock = pygame.time.Clock()
framerate = 60

# Sprites
puppy_sprite = pygame.transform.scale(pygame.image.load('M/Puppy.gif'), (64, 64))
Spuppy_sprite = pygame.transform.scale(pygame.image.load('M/Strong Puppy.png'), (64, 64))
puppy_rect = puppy_sprite.get_rect(center=(40, 80))
Spuppy_rect = Spuppy_sprite.get_rect(center=(40, 160))

# Game state
score = 200
networth = 200
displayed_score = 200
displayed_networth = 200
puppy_value = 1
Spuppy_value = 5
puppy_cost = 100
steroid_cost = 100
puppy_amount = 0
puppy_speed = 1
Spuppy_speed = 0.5
current_puppy_speed = puppy_speed
draw_puppy = False
draw_Spuppy = False
puppy_length = 0
Spuppy_length = 0
opaque_gray_length = 0
opaque_gray_speed = 1
bought = False
buy_puppy = False
opacity = 0

# Steroid effect
steroid_active = False
steroid_timer = 0

# ------------------------ Functions ------------------------

def draw_task(sprite, color, y_coord, button_money, draw, length, speed, networth, score):
    if draw and length < 180:
        length += speed
    elif draw:
        draw = False
        length = 0
        score += button_money
        networth += button_money

    pygame.draw.rect(screen, color, [70, y_coord - 15, 180, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 170, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])

    return pygame.Rect(10, y_coord - 20, 40, 40), length, draw, networth, score

def draw_sprite_labels():
    screen.blit(puppy_sprite, puppy_rect)
    screen.blit(Spuppy_sprite, Spuppy_rect)
    screen.blit(font.render("$1 stupid puppy", True, white), (70, 40))
    screen.blit(font.render("$5 strong puppy", True, white), (70, 120))

def steroid_boost(score, button_clicked, steroid_cost, steroid_active, steroid_timer,opacity):

    if steroid_active == True and button_clicked == True:

        opacity += 1
        fade_in_animation = pygame.Surface((150, 100), pygame.SRCALPHA)
        fade_in_animation.fill((red, opacity))


    else:
        button = pygame.draw.rect(screen,red, [30,370, 150, 100])
        opacity = 255



    screen.blit(font.render("Steroids", True, white), (30, 370))
    screen.blit(font.render(f"${round(steroid_cost, 2)}", True, green), (50, 300))

    if button_clicked and score >= steroid_cost:
        score -= steroid_cost
        steroid_cost *= 2
        steroid_active = True
        steroid_timer = 60 * framerate
        button_clicked = False

    return button, steroid_cost, score, button_clicked, steroid_active, steroid_timer,opacity

def puppy_upgrade(x_coord, score, puppy_cost, puppy_amount, buy_puppy):
    button = pygame.draw.rect(screen, gray, [x_coord, 340, 150, 100])
    screen.blit(font.render(f"${round(puppy_cost, 2)}", True, green), (x_coord + 35, 290))

    if buy_puppy and score >= puppy_cost:
        puppy_amount += 1
        score -= puppy_cost
        buy_puppy = False  # Reset the flag

    puppy_cost = (100 * (1.15 ** puppy_amount))
    screen.blit(font.render(f"small puppies {puppy_amount}", True, white), (x_coord + 5, 350))
    return button, puppy_cost, puppy_amount, score, buy_puppy



def money_loop(color, y_coord, length, speed, score, amount, networth, steroid_active):
    bar_surface = pygame.Surface((length, 30), pygame.SRCALPHA)
    bar_surface.fill((*color, 150))
    screen.blit(bar_surface, (70, y_coord - 15))

    # Apply steroid speed multiplier
    if steroid_active:
        speed *= 10
    if length < 180:
        length += speed
    else:
        length = 0
        score += amount
        networth += amount

    return length, score, networth


# ------------------------ Game Loop ------------------------

running = True
while running:
    clock.tick(framerate)
    screen.fill(black)

    draw_sprite_labels()

    # Apply and Disable steroid effect
    if steroid_active:
        screen.blit(font.render("Steroid active", True, white), (70, 40))
        current_puppy_speed = puppy_speed * 10
        steroid_timer -= 1
        if steroid_timer <= 0:
            steroid_active = False
    else:
        current_puppy_speed = puppy_speed

    # Passive income from puppies
    if puppy_amount >= 1:
        opaque_gray_length, score, networth = money_loop(gray, 50, opaque_gray_length, opaque_gray_speed, score, puppy_amount, networth,steroid_active)

    # Tasks
    task1, puppy_length, draw_puppy, networth, score = draw_task(puppy_sprite, gray, 80, puppy_value, draw_puppy, puppy_length, current_puppy_speed, networth, score)
    task2, Spuppy_length, draw_Spuppy, networth, score = draw_task(Spuppy_sprite, orange, 160, Spuppy_value, draw_Spuppy, Spuppy_length, Spuppy_speed, networth, score)

    # UI buttons
    steroid_button, steroid_cost, score, bought, steroid_active, steroid_timer,opacity = steroid_boost(score, bought, steroid_cost, steroid_active, steroid_timer,opacity)
    puppy_button, puppy_cost, puppy_amount, score, buy_puppy = puppy_upgrade(800, score, puppy_cost, puppy_amount,buy_puppy)

    # Score animation
    displayed_score += min(1, score - displayed_score) if displayed_score < score else -min(1, displayed_score - score)
    displayed_networth += min(1, networth - displayed_networth) if displayed_networth < networth else -min(1, displayed_networth - networth)

    screen.blit(font.render(f"$ {round(displayed_score, 2)}", True, white), (650, 50))
    screen.blit(font.render(f"Total Earned: $ {round(displayed_networth, 2)}", True, white), (650, 80))
    screen.blit(font.render(str(pygame.mouse.get_pos()), True, white), (800, 50))



    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if puppy_rect.collidepoint(event.pos): draw_puppy = True
            if Spuppy_rect.collidepoint(event.pos): draw_Spuppy = True
            if puppy_button.collidepoint(event.pos):
                buy_puppy = True
            if steroid_button.collidepoint(event.pos) and score >= steroid_cost:
                bought = True

    pygame.display.flip()

pygame.quit()
