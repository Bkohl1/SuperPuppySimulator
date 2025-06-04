# display.py
import pygame
import Main
pygame.init()

screen = pygame.display.set_mode((1000, 800))
font = pygame.font.SysFont("bahnschrift", 30)
screen.blit(puppy_sprite, puppy_rect)
screen.blit(Spuppy_sprite, Spuppy_rect)
screen.blit(font.render("$1 stupid puppy", True, white), (70, 40))
screen.blit(font.render("$5 strong puppy", True, white), (70, 120))

clock.tick(framerate)
screen.fill(black)
def draw_task(sprite, color, y_coord, button_money, draw, length, speed, networth, score):
    if draw and length < 180:
        length += speed
    elif draw:
        draw = False
        length = 0
        score += button_money
        networth += button_money

    pygame.draw.rect(screen, color, [70, y_coord - 15, 180, 30])
    pygame.draw.rect(screen,(0,0,0), [75, y_coord - 10, 170, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])