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
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += 10
    def update2(self):
        keys_pressed = key.get_pressed()       
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += 10
        
    

"""class Ball(GameSprite):
    def update(self):"""
        
clock = time.Clock()
FPS = 60

game = True
finish = False
rocketl = Player('L.png',100,150,5,35,150)
rocketr = Player('R.png',550,150,5,35,150)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(bg,(0,0))
        
        
        rocketl.update()
        rocketl.reset()
        
        rocketr.update2()
        rocketr.reset()
        
        
        
        clock.tick(FPS)
        display.update()
        
        
    
