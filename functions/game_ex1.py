import pgzrun

HEIGHT = 300                      # sets the size of window
WIDTH = 800
p=Actor('ironman', (100,100))     # actor checks whether there is a file of ironman or not
c=Actor('cookie')

def draw():
    screen.fill('white')
    p.draw()                       # two functions in gaming program w/o which it doesn't run that are draw and update function
    c.draw()
    print('drawing')

def update():
    print('updating')
    p.x-=2
    p.angle= -10
    if p.x<0:
        p.x=WIDTH
    print(p.x,p.y)

pgzrun.go()