import Score
class Upgrade:
    def __init__(self, networth, score,upgrade_price):

        #from Score class:
        self.networth = networth
        self.score = score

        #native to Upgrade class
        self.upgrade_price = upgrade_price

    def Buy_Upgrade(self):
        if self.score >= self.upgrade_price:
            self.score -= self.upgrade_price

    def puppy_upgrade(x_coord, score, puppy_cost, puppy_amount, buy_puppy):
        button = pygame.draw.rect(screen, gray, [x_coord, 340, 150, 100])
        screen.blit(font.render(f"${round(puppy_cost, 2)}", True, green), (x_coord + 35, 290))

        if buy_puppy and score >= puppy_cost:
            puppy_amount += 1
            score -= puppy_cost
            buy_puppy = False  # Reset the flag

        puppy_cost = (100 * (1.15 ** puppy_amount))
        screen.blit(font.render(f"small puppies {puppy_amount}", True, white), (x_coord + 5, 350))
        return button, puppy_cost, puppy_amount, score, buy_puppy