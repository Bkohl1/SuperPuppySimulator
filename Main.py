import display
import Score
import Colors
import Button
import pygame

clock = pygame.time.Clock()
framerate = 60
screen = display.screen
font = display.font



# Sprites
puppy_sprite = pygame.transform.scale(pygame.image.load('M/Puppy.gif'), (64, 64))
Spuppy_sprite = pygame.transform.scale(pygame.image.load('M/Strong Puppy.png'), (64, 64))
puppy_rect = puppy_sprite.get_rect(center=(40, 80))
Spuppy_rect = Spuppy_sprite.get_rect(center=(40, 160))