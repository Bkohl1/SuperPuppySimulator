# display.py
import pygame
import Button

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

#button variables
length = 180



#this class initializes the screen/window


font = pygame.font.SysFont("comicsans", 15)

def load_sprites():
    puppy_sprite = pygame.transform.scale(pygame.image.load('M/Puppy.gif'), (64, 64))
    Spuppy_sprite = pygame.transform.scale(pygame.image.load('M/Strong Puppy.png'), (64, 64))
    Mpuppy_sprite = pygame.transform.scale(pygame.image.load('M/Mega Puppy.jpg'), (64, 64))
    Super_puppy_sprite = pygame.transform.scale(pygame.image.load('M/Super Puppy.jpg'), (64, 64))
    puppy_rect = puppy_sprite.get_rect(center=(40, 80))
    Spuppy_rect = Spuppy_sprite.get_rect(center=(40, 160))
    Mpuppy_rect = Mpuppy_sprite.get_rect(center=(40, 240))
    Super_puppy_rect = Super_puppy_sprite.get_rect(center=(40, 320))
    return puppy_sprite, Spuppy_sprite, Mpuppy_sprite,Super_puppy_sprite,puppy_rect, Spuppy_rect,Mpuppy_rect,Super_puppy_rect

def display_sprites(puppy_sprite, puppy_rect, Spuppy_sprite, Spuppy_rect,Mpuppy_sprite, Mpuppy_rect,Super_puppy_sprite, Super_puppy_rect,screen):
    screen.blit(puppy_sprite, puppy_rect)
    screen.blit(Spuppy_sprite, Spuppy_rect)
    screen.blit(Mpuppy_sprite, Mpuppy_rect)
    screen.blit(Super_puppy_sprite, Super_puppy_rect)
    screen.blit(font.render("$1 stupid puppy", True, (gray)), (90, 40))
    screen.blit(font.render("$5 strong puppy", True, (brown)), (90, 120))
    screen.blit(font.render("$20 mega puppy", True, (red)), (90, 200))
    screen.blit(font.render("$100 super puppy", True, (blue)), (90, 280))

    return puppy_rect, Spuppy_rect,Mpuppy_rect,Super_puppy_rect

def bar_animation(y_coord, color, screen, length, speed, check_click, bar_finish):
    if length < 180:
        length += speed
        check_click = True
        bar_finish = False
    elif length >= 180:
        length = 0
        check_click = False
        bar_finish = True

    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    return check_click, length, bar_finish


def display_buttons(screen,y_coord,color,length):
    pygame.draw.rect(screen, color , [70, y_coord - 15, 180, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 170, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])







