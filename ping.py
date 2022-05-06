from pygame import *
w = 700
h = 500


window = display.set_mode((w,h))
bg = transform.scale(image.load('bg.png'),(w,h))
display.set_caption("Ping-pong")
class GameSprite(sprite.Sprite):
    def __init__(self, img, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()       
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_s] and self.rect.x < 625:
            self.rect.x += 10
"""class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > w:"""
clock = time.Clock()
FPS = 60

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(bg,(0,0))
        clock.tick(FPS)
        
        
        
        
        display.update()
        
        
    