import display
import Score
import Colors
import Button
import pygame
import Soundfx

pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
light_gray = (140, 140, 140)
orange = (255, 165, 0)
brown = (150, 75, 0)
blue = (0, 0, 255)

Puppy_click = False
SPuppy_click = False
MPuppy_click = False
Super_Puppy_click = False
change_name = False
egg_click = False
egg_show = True

bar_finish = False



length = 0
Pbar_length = 0
SPbar_length = 0
MPbar_length = 0
Super_Pbar_length = 0

#Button speeds
Puppy_speed = Button.Puppy.speed
SPuppy_speed = Button.SPuppy.speed
MPuppy_speed = Button.MPuppy.speed
Super_Puppy_speed = Button.Super_Puppy.speed


clock = pygame.time.Clock()
framerate = 60
font = pygame.font.SysFont("AdobeGothicStd-Bold", 15)
stats_font = pygame.font.SysFont("AdobeGothicStd-Bold", 20)
screen = pygame.display.set_mode((1000, 800))
screen.fill(black)




# Load sprites
puppy_sprite, Spuppy_sprite, Mpuppy_sprite,Super_puppy_sprite,puppy_rect, Spuppy_rect,Mpuppy_rect,Super_puppy_rect = display.load_sprites()

# Create Score instance
score_obj = Score.Score()

running = True
while running:
    screen.fill((0, 0, 0))  # Prevent trails
    display.display_sprites(puppy_sprite, puppy_rect, Spuppy_sprite, Spuppy_rect, Mpuppy_sprite, Mpuppy_rect,Super_puppy_sprite, Super_puppy_rect,screen)

    display.display_buttons(screen,80, gray,length,'Buy 1 trainer')
    display.display_buttons(screen, 160,brown,length,'Buy 1 steroids')
    display.display_buttons(screen, 240,red,length,'Buy 1 amphetamine')
    display.display_buttons(screen, 320, blue, length,'Buy 1 super dog')



    #Display army name
    army_name,army_name_rect = display.display_army_name(screen,'bretts dog army',300)


    if not egg_click and egg_show:
        # Display Easter Egg
        egg_text, egg_rect = display.display_egg(screen, 'Click if you think this game is stupid', 600, 110)




    # Update and draw the score
    score_obj.update_display(screen, stats_font,white)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if puppy_rect.collidepoint(event.pos) and not Puppy_click:
                Puppy_click = True
            if Spuppy_rect.collidepoint(event.pos) and not SPuppy_click:
                SPuppy_click = True
            if Mpuppy_rect.collidepoint(event.pos) and not MPuppy_click:
                MPuppy_click = True
            if Super_puppy_rect.collidepoint(event.pos) and not Super_Puppy_click:
                Super_Puppy_click = True
            if egg_rect.collidepoint(event.pos) and not egg_click:
                egg_click = True


    if Puppy_click:
        bar_finish = False
        prev_length = Pbar_length
        Puppy_click, Pbar_length,bar_finish = display.bar_animation(80, light_gray, screen, Pbar_length, Puppy_speed, Puppy_click,bar_finish)
        if bar_finish == True and SPbar_length < 180:
            bar_finish = False
            Soundfx.minecraft_bark()
            score_obj.add_money(1)
            score_obj.update_display(screen, font, white)

    if SPuppy_click:
        prev_length = SPbar_length
        SPuppy_click, SPbar_length,bar_finish = display.bar_animation(160, brown, screen, SPbar_length, SPuppy_speed,SPuppy_click,bar_finish)
        if bar_finish == True and SPbar_length < 180:
            bar_finish = False
            Soundfx.Spuppy_bark()
            score_obj.add_money(5)
            score_obj.update_display(screen, font, white)

    if MPuppy_click:
        bar_finish = False
        prev_length = MPbar_length
        MPuppy_click, MPbar_length,bar_finish = display.bar_animation(240, red, screen, MPbar_length, MPuppy_speed,MPuppy_click,bar_finish)
        if bar_finish == True and SPbar_length < 180:
            bar_finish = False
            Soundfx.MPuppy_bark()
            score_obj.add_money(20)
            score_obj.update_display(screen, font, white)

    if Super_Puppy_click:
        bar_finish = False
        prev_length = Super_Pbar_length
        Super_Puppy_click, Super_Pbar_length,bar_finish = display.bar_animation(320, blue, screen, Super_Pbar_length,Super_Puppy_speed, Super_Puppy_click,bar_finish)
        if bar_finish == True  and SPbar_length < 180:
            bar_finish = False
            Soundfx.Super_Puppy_bark()
            score_obj.add_money(100)
            score_obj.update_display(screen, font, white)

    if egg_click and egg_show:
        Soundfx.syfm()
        egg_show = False



    pygame.display.flip()


pygame.quit()
