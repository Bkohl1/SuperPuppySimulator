class Score:
    def __init__(self, money=200, score=200, networth=200):
        self.money = money
        self.score = score
        self.networth = networth
        self.displayed_score = float(score)
        self.displayed_networth = float(networth)
        self.displayed_money = float(money)

    def add_money(self, amount):
        self.money += amount
        self.score += amount
        self.networth += amount

    def update_display(self, screen, font, white):
        # Animate score smoothly (10% of the difference each frame)
        self.displayed_score += (self.score - self.displayed_score) * .01
        self.displayed_networth += (self.networth - self.displayed_networth) * .01
        self.displayed_money+= (self.money - self.displayed_money) * .01

        # Optional: show current balance
        screen.blit(font.render(f"Money: $ {round(self.displayed_money)}", True, white), (650, 20))
        screen.blit(font.render(f"Game Score: {round(self.displayed_score)}", True, white), (650, 50))
        screen.blit(font.render(f"Total Earned: $ {round(self.displayed_networth)}", True, white), (650, 80))
