import pygame

pygame.init()

click = pygame.mixer.Sound("Sfx/ding.mp3")
dogpant = pygame.mixer.Sound("Sfx/dogpant.mp3")
minecraftBark = pygame.mixer.Sound("Sfx/minecraft_dog_bark.mp3")
minecraftPant = pygame.mixer.Sound("Sfx/minecraft_dog_pant.mp3")
lvlup = pygame.mixer.Sound("Sfx/dog_level_up.mp3")
hit = pygame.mixer.Sound('Sfx/hitmarker.mp3')
Syfm = pygame.mixer.Sound('Sfx/syfm.mp3')
strong_puppy_bark = pygame.mixer.Sound("Sfx/minecraft_lowdog_bark1.mp3")
Mega_puppy_bark = pygame.mixer.Sound("Sfx/mega_dog_bark.mp3")
Super_puppy_bark = pygame.mixer.Sound("Sfx/super_dog_bark.mp3")

def ding():
    click.play()

def dogpant():
    dogpant.play()

def minecraft_bark():
    minecraftBark.play()

def Spuppy_bark():
    strong_puppy_bark.play()

def MPuppy_bark():
    Mega_puppy_bark.play()

def Super_Puppy_bark():
    Super_puppy_bark.play()

def minecraft_pant():
    minecraftPant.play()

def dog_lvl_up():
    lvlup.play()

def hitmarker():
    hit.play()

def syfm():
    Syfm.play()
