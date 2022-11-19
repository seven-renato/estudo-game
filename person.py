from graphics import *
from time import *
class Mario:
    def __init__(self, x, y, win,raio):
        self.x = x
        self.y = y
        self.win = win
        self.Mario = Image(Point(100,300),"./assets/mario/mario_lwalk0.png")
        self.Mario.draw(win)
        self.velocidadeY = -5
        self.raio = raio
        self.numPulos = 0
        self.lado = False
        self.contR = 0
    def move(self):
        center = self.Mario.getAnchor()
        tecla = self.win.checkKey()
        if tecla == 'd':
            self.contR += 1
            if self.contR == 5:
                self.Mario.undraw()
                self.Mario = Image(center,"./assets/mario/mario_rwalk1.png")
                self.Mario.draw(self.win)
                update(30)
                self.contR = 0
            self.Mario.move(10, -4)
            self.lado = False
        if tecla == 'a':
            self.Mario.undraw()
            self.Mario = Image(center,"./assets/mario/mario_lwalk1.png")
            self.Mario.draw(self.win)
            update(60)
            self.Mario.move(-10, 0)
            self.lado = True
        if tecla == 'w':
            self.jump()
    def jump(self):
        center = self.Mario.getAnchor()
        vet = [Image(center, "./assets/mario/mario_Ljump.png"),Image(center, "./assets/mario/mario_Rjump.png")]
        if self.numPulos == 0:
            if self.lado:
                self.Mario.undraw()
                self.Mario = vet[0]
                self.Mario.draw(self.win)
            else:
                self.Mario.undraw()
                self.Mario = vet[1]
                self.Mario.draw(self.win)
            self.velocidadeY += -5
            self.Mario.move(0,-7)
            self.numPulos += 1

    def gravidade(self):
        # Check se tem chao, se tiver, vc coloca a velocidadeY = 0
        center = self.Mario.getAnchor()
        posy = center.getY()
        if posy + self.raio -1 > 500:
            self.velocidadeY = 0
            self.numPulos = 0
            if self.lado:
                self.Mario.undraw()
                self.Mario = Image(center,"./assets/mario/mario_lwalk0.png")
                self.Mario.draw(self.win)
            else:
                self.Mario.undraw()
                self.Mario = Image(center,"./assets/mario/mario_Rwalk0.png")
                self.Mario.draw(self.win)                   
        self.Mario.move(0, self.velocidadeY)
        self.velocidadeY += 0.3

    def undraw(self):
        self.Mario.undraw()
        pass