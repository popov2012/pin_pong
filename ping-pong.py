from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (0, 255, 0))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.SysFont('Arial', 36)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"
img_bullet = "bullet.png"
img_hero = "rocket.png"
img_enemy = "ufo.png"
img_asteroid = "asteroid.png"

score = 0
goal = 20
lost = 0
max_lost = 10
cbullets = 5
reload_timer = 0
reloading = False
lives = 3
super_bullet_active = False
super_bullet_rect = None
super_bullet_cooldown = False
super_bullet_cooldown_timer = 0

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed

       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_s] and self.rect.x > 5:
           self.rect.y -= self.speed
       if keys[K_w] and self.rect.x < win_width - 80:
           self.rect.y += self.speed

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

finish = False
run = True

while run:
    for e in event.get():
        keys = key.get_pressed()
        if e.type == QUIT:
            run = False
    if not finish:
       window.blit(background,(0,0))

       ship.update()

    time.delay(50)
#w