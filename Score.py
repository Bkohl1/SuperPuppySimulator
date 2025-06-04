#This class holds the value of the score, as well as networth, achievements, and conditions for upgrades.
import pygame
pygame.init()

class Score:
    def __init__(self,money,score,condition,networth):
        self.money = money
        self.score = score
        self.condition = condition
        self.networth = networth

    def accumulate_networth(self):
        displayed_networth = self.networth


        displayed_networth += min(1, self.networth - displayed_networth) if displayed_networth < self.networth else -min(1,displayed_networth - self.networth)

    def accumulate_score(self):
        displayed_score = self.score
        self.networth += self.money - self.networth

        displayed_score += min(1, self.score - displayed_score) if displayed_score < self.score else -min(1,displayed_score - self.score)

        screen.blit(font.render(f"$ {round(displayed_score, 2)}", True, white), (650, 50))
        screen.blit(font.render(f"Total Earned: $ {round(displayed_networth, 2)}", True, white), (650, 80))


        return self.score,self.networth








networth = Score(0,0,False)


