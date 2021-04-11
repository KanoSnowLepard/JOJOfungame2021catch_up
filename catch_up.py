from pygame import *

window = display.set_mode((728, 410))
display.set_caption("dogoni")

background = transform.scale(image.load("gg.jpg"), (728, 410))

clock = time.Clock()
FPS = 60

sprite1 = transform.scale(image.load("dio2.png"), (100,100))
sprite2 = transform.scale(image.load("jotaro2.png"), (100,100))
x1 = 200
y1 = 200
x2 = 400
y2 = 200
game = True 
while game:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y1 > 5 :
        y1 -= 10 
    if keys_pressed[K_DOWN] and y1 < 285:
        y1 += 10 
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= 10 
    if keys_pressed[K_RIGHT] and x1  < 615:
        x1 += 10 
    
    if keys_pressed[K_s] and y2 < 285:
        y2 += 10
    if keys_pressed[K_w] and y2 > 5:
        y2 -= 10
    if keys_pressed[K_a] and x2 > 5:
        x2 -= 10
    if keys_pressed[K_d] and x2 < 615:
        x2 += 10
    window.blit(background, (0, 0))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)