import pygame, random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tracker")

class Bot:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.weighted_directions = [(1, 'LEFT'), (1, 'RIGHT'), (1, 'UP'), (1, 'DOWN')]

    def draw(self):
        pygame.draw.rect(win, (self.color[0], self.color[1], self.color[2]), (self.x, self.y, self.width, self.height))

    def move(self):
        if fruit.x > self.x:
            self.x += 1
        if fruit.x < self.x:
            self.x -= 1
        if fruit.y > self.y:
            self.y += 1
        if fruit.y < self.y:
            self.y -= 1

    def color_change(self):
        self.color[0] %= 255
        self.color[0] += 1

        self.color[1] %= 255
        self.color[1] += 1

        self.color[2] %= 255
        self.color[2] += 1


class Fruit:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def respawn(self):
        self.x = random.randint(1, 480)
        self.y = random.randint(1, 480)


bot = Bot(250, 250, [60, 120, 180], 20, 20)
fruit = Fruit(100, 250, (0, 0, 0), 20, 20)

running = True
while running:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #win.fill((0, 0, 0))
    bot.move()
    bot.color_change()
    if abs((fruit.x + 10) - (bot.x + 10)) < 5 and abs((fruit.y + 10) - (bot.y + 10)) < 5:
        fruit.respawn()
    fruit.draw()
    bot.draw()
    pygame.display.update()

pygame.quit()
