from pygame import *
from random import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,size_w, size_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_w , size_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.direction = "left"
        self.rect.x = player_x
        self.rect.y = player_y
         
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bulletBloodborne.png", self.rect.centerx, self.rect.top, 15, 25, 15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.direction ="down"
        global lose
        if self.rect.y >500:
            lose += 1
            self.rect.y = 0
            self.rect.x = randint(80, 620)
monster = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

bullets = sprite.Group()
for i in range(6):
    monster.add(Enemy("enemy" + str(i + 1)+".png", randint(80,620), 0 ,110, 100,randint(1,2)))
    

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("galaxyfight")

player = Player("ggg.png", 5 , win_height - 100,50,100, 10)

background = transform.scale(image.load("bliad.png"), (win_width, win_height))
lose = 0 
score = 0


mixer.init()
mixer.music.load("saito-tsukasa-cleric-beast.ogg")
mixer.music.play()
bulletsound = mixer.Sound("bullet sound.ogg")  

font.init()
font1 = font.SysFont("Arial.ttf", 33)
font2 = font.SysFont("Arial.ttf", 33)


game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT :
            game == False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                bulletsound.play()
                player.fire()
    sprite_list = sprite.groupcollide( monster, bullets, True, True)
    for s in sprite_list:
        score += 1
        monster.add(Enemy("enemy" + str(i + 1)+".png", randint(80,620), 0 ,110, 100,randint(1,2)))
    if lose > 3 or sprite.spritecollide(player ,monster, False):
        game = False


    window.blit(background, (0,0))
    player.reset()
    player.update()
    bullets.update()
    bullets.draw(window)
    monster.update()
    monster.draw(window)
    text_lose = font1.render("Пропущено:" + str(lose), 1 ,(255,0,255))
    text_score = font2.render("Очки:" + str(score), 1 ,(255,0,255))
    window.blit(text_lose,(5,5))
    window.blit(text_score,(5,25))
    display.update()
    clock.tick(FPS)