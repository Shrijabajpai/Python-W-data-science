import pgzrun

WIDTH=1200
HEIGHT=600

scr=0

def gamescr(bgcolor,title,info):
    screen.fill(bgcolor)
    screen.draw.text(title,center=(WIDTH/2,HEIGHT/2),fontsize=100,color='white',align='center')
    screen.draw.text(info,center =(WIDTH/2,HEIGHT/2+100),fontsize=80,color='white',align='center')


def draw():
    if scr==0:
        gamescr('black','Amazing Game','Press Space To Start')
    elif scr==1:
        gamescr('green','Game Us Running','Press esc To end Game')
    elif scr==2:
        gamescr('blue','Game Over','Press enter To Restart')

def update():
    global scr  
    if keyboard.space and scr==0: 
        scr=1 
    elif keyboard.escape and scr==1:
        scr=2 
    elif keyboard.Return and scr==2:
        scr=0                           
         
pgzrun.go()