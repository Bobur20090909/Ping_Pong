from pygame import *

window = display.set_mode((700,500))

display.set_caption("Пинг Понг")
background = transform.scale(image.load("background1.jpg"), (700,500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, x, y, width, height,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    pass
ball = GameSprite('sprites_7.png', 200,200, 100, 100, 5)
game = True
while game:
    window.blit(background,(0,0))
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
        # if e.type == MOUSEMOTION:

    display.update()
    clock.tick(60)
