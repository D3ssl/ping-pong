from pygame import *
font.init()
w = 700
h = 500
font1 = font.Font(None,30)

lose1 = font1.render("Player 1 lose",1,(255,255,255))
lose2 = font1.render("Player 2 lose",1,(255,255,255))





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
        if keys_pressed[K_w] and self.rect.y > 15:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 335:
            self.rect.y += 10
    def update2(self):
        keys_pressed = key.get_pressed()       
        if keys_pressed[K_UP] and self.rect.y > 15:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 335:
            self.rect.y += 10
        
        
        
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

game = True
finish = False
rocket1 = Player('L.png',50,150,5,35,150)
rocket2 = Player('R.png',620,150,5,35,150)
ball = GameSprite("ball.png",310,175,0,65,65)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(bg,(0,0))
        
        ball.reset()
        
        
        rocket1.update()
        rocket1.reset()
        
        rocket2.update2()
        rocket2.reset()
        
        
    
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if ball.rect.y > h-65 or ball.rect.y < 0:
            speed_y *= -1
     
        
        if sprite.collide_rect(rocket1,ball) or sprite.collide_rect(rocket2,ball):
            speed_x *= -1
            
        
        
        
        
        
        clock.tick(FPS)
        display.update()
        
        
    
