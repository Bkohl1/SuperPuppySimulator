import pygame
import display
import Colors

screen = display.screen
font = display.font
white = Colors.white

class Score:
    def __init__(self, money=0, score=0, condition=False, networth=0):
        self.money = money
        self.score = score
        self.condition = condition
        self.networth = networth
        self.displayed_score = 0
        self.displayed_networth = 0

    def accumulate_networth(self):
        self.networth += self.money

    def update_display(self):
        if self.displayed_score < self.score:
            self.displayed_score += min(1, self.score - self.displayed_score)
        elif self.displayed_score > self.score:
            self.displayed_score -= min(1, self.displayed_score - self.score)

        if self.displayed_networth < self.networth:
            self.displayed_networth += min(1, self.networth - self.displayed_networth)
        elif self.displayed_networth > self.networth:
            self.displayed_networth -= min(1, self.displayed_networth - self.networth)

        screen.blit(font.render(f"$ {round(self.displayed_score, 2)}", True, white), (650, 50))
        screen.blit(font.render(f"Total Earned: $ {round(self.displayed_networth, 2)}", True, white), (650, 80))
