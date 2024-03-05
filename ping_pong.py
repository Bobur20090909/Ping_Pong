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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 250:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 250:
            self.rect.y += self.speed


ball = GameSprite('sprites_7.png', 50,50, 50, 50, 12)
player_l = Player("sprites_5.png", 5, 50, 40, 250, 4)
player_r = Player("sprites_6.png", 655, 50, 40, 250, 4)
game = True
finish = False
speed_x = 3
speed_y = 3

while game:    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1
        
        window.blit(background,(0,0))
        ball.reset()
        player_l.reset()
        player_l.update_l()
        player_r.reset()
        player_r.update_r()


        # if e.type == MOUSEMOTION:

    display.update()
    clock.tick(60)
