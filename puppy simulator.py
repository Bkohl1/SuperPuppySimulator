



# Game state
#score = 200
#networth = 200
#displayed_score = 200
#displayed_networth = 200

#puppy_value = 1
#Spuppy_value = 5
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

"""

    return pygame.Rect(10, y_coord - 20, 40, 40), length, draw, networth, score"""


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





def money_loop(color, y_coord, length, speed, score, amount, networth, steroid_active):


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
