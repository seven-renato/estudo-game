from graphics import *
from person import *

win = GraphWin("Donkey Kong",600,686, autoflush=False)
cenario = Image(Point(300,343),"./assets/cenario.png")
cenario.draw(win)


mario_lwalks = ["./public/mario/mario_lwalk0.png","./public/mario/mario_lwalk1.png","./public/mario/mario_lwalk2.png"]
mario_rwalks = ["./public/mario/mario_rwalk0.png","./public/mario/mario_rwalk1.png","./public/mario/mario_rwalk2.png"]

p1 = Mario(250, 250, win, 25)
chao = Line(Point(0, 500), Point(700, 500) )
chao.draw(win)


while not win.isClosed():
    p1.move()
    p1.gravidade()
    update(60)
win.close()