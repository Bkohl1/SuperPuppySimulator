#This class holds the button attributes: amount, button value, speed.
#This class also holds the function to deploy the steroid and tired effect to the button's speed and value.
import pygame
pygame.init()

class Button:
    def __init__(self,amount,button_value,speed):
        self.amount = amount
        self.button_value = button_value
        self.speed = speed

        #applies the steroid effect to the different puppies
    def steroid_effect(self):
        self.speed *= 10
        self.button_value *= 10

    def tired_defect(self):
        self.speed /= 2
        self.button_value /= 2

    def tired_end(self):
        self.speed *= 2
        self.button_value *= 2

    def steroid_end(self):
        self.speed /= 10
        self.button_value /= 10


Puppy = Button(0,1,1)
SPuppy = Button(0,5,.5)
