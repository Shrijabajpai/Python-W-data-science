import pygame
import pgzrun
from random import randint

HEIGHT=600
WIDTH=1200
p=Actor('ironman',center=(WIDTH//2,HEIGHT//2))
c=Actor('cookie',(randint(0,WIDTH),randint(0,HEIGHT)))

title='IRON-MAN GAME'
score = 0
music.play('mc')                           
music.set_volume(0.5) 


def draw():
    screen.fill('white')
    screen.blit('img',(0,0))
    screen.draw.text(title,center=(WIDTH//2,30),fontsize=60,color='black',align='center',shadow=(.2,1),scolor='red')
    screen.draw.text(f'score:{score}',(10,10),fontsize=40,color='black')
    p.draw()
    c.draw()
    
def p_move():
    '''function to move player'''
    if keyboard.left and p.left > 0 :
        p.x -= 3
        p.angle=10
    elif keyboard.right and p.right < WIDTH :
        p.x += 3
        p.angle= -10
    elif keyboard.up and p.top > 0:
        p.y -= 3
    elif keyboard.down and p.bottom < HEIGHT:
        p.y += 3
    else:
        p.angle=0


def update():
    global score
    p_move()
    if p.colliderect(c):                                               
        score += 1
        c.pos = (randint(0,WIDTH),(randint(0,HEIGHT)))     
        sounds.sound.play(100)  
    print(p.x,p.y)
    print(p.x,p.y,p.angle)
    if keyboard.f:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()
pgzrun.go()