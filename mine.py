import pygame as pg
import random
import time

pg.init()
pg.font.init()

font = pg.font.SysFont("mont.ttf", 50)

#Settings
winx = 450
winy = 450
FPS = 60

class Polje:
    def __init__(self, x, y, color, isBomb):
        self.x = x
        self.y = y
        self.color = color
        self.number = random.randint(1, 3)
        self.isBomb = isBomb
        self.clickable = True

class Text:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

#Polja
mines = [[Polje(0,0, "light grey", False)],
         [Polje(0,50, "grey", False)],
         [Polje(0, 100, "light grey", False)],
         [Polje(0, 150, "grey", False)],
         [Polje(0, 200, "light grey", False)],
         [Polje(0, 250, "grey", False)],
         [Polje(0, 300, "light grey", False)],
         [Polje(0, 350, "grey", False)],
         [Polje(0, 400, "light grey", False)],
         ]

texts = []

for i in range(len(mines)):
    for j in range(1, 10):

        willBomb = False

        if random.randint(1,10) == 2:
            willBomb = True

        if mines[i][j - 1].color == "light grey":
            mines[i].append(Polje(mines[i][j - 1].x + 50, mines[i][j - 1].y, "grey", willBomb))
        elif mines[i][j - 1].color == "grey":
            mines[i].append(Polje(mines[i][j - 1].x + 50, mines[i][j - 1].y, "light grey", willBomb))

bombs = []

for i in range(10):
    bomb = random.randint(1, 50)
    print(bomb//10, bomb%10)
    mines[bomb//10 - 1][bomb % 10 - 1].secretColor = "red"
    bombs.append(mines[bomb//10 - 1][bomb % 10 - 1])     

#Display
display = pg.display.set_mode((winx, winy))

game = True
end = False

discovered = 0

while game:
    #Clock
    pg.time.Clock().tick(FPS)

    display.fill("white")

    if discovered - len(mines) >= 81:
        game = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mousePos = pg.mouse.get_pos()

            numMines = 0

            for i in mines:
                for j in i:

                    if j.isBomb:
                        j.color = "red"

                    if mousePos[0] >= j.x and mousePos[0] <= j.x + 50 and mousePos[1] >= j.y and mousePos[1] <= j.y + 50 and j.clickable:
                        j.clickable = False

                        if j.isBomb:
                            j.color = "red"
                            pg.display.update()
                            time.sleep(0.2)
                            game = False

                        #LEVO IN DESNO
                        if i.index(j) + 1 < len(i):
                            if i[i.index(j) + 1].isBomb:
                                numMines += 1
                        if i.index(j) - 1 < len(i):
                            if i[i.index(j) - 1].isBomb:
                                numMines += 1

                        #GOR IN DOL
                        if mines.index(i) + 1 <= len(mines) - 1:
                            if mines[mines.index(i) + 1][i.index(j)].isBomb:
                                numMines += 1

                        if mines.index(i) - 1 >= 0:
                            if mines[mines.index(i) - 1][i.index(j)].isBomb:
                                numMines += 1

                            #GOR LEVO
                        if mines.index(i) - 1 <= len(mines) - 1 and i.index(j) - 1 < len(i):
                            if mines[mines.index(i) - 1][i.index(j) - 1].isBomb:
                                numMines += 1
                            #GOR DESNO
                        if mines.index(i) - 1 <= len(mines) - 1 and i.index(j) + 1 < len(i):
                            if mines[mines.index(i) - 1][i.index(j) + 1].isBomb:
                                numMines += 1
                            #DOL LEVO
                        if mines.index(i) + 1 <= len(mines) - 1 and i.index(j) - 1 < len(i):
                            if mines[mines.index(i) + 1][i.index(j) - 1].isBomb:
                                numMines += 1
                            #DOL DESNO
                        if mines.index(i) + 1 <= len(mines) - 1 and i.index(j) + 1 < len(i):
                            if mines[mines.index(i) + 1][i.index(j) + 1].isBomb:
                                numMines += 1

                        discovered += 1

                        texts.append(Text(j.x + 15, j.y + 10, numMines))

                        
                        
                        
                        
    for lane in mines:
        for mine in lane:
            pg.draw.rect(display, mine.color, (mine.x, mine.y, 50, 50))

    for text in texts:
        textt = font.render(f"{text.text}", True, "black", None)
        display.blit(textt, (text.x, text.y))    
    
    #Update
    pg.display.update()

    if end == True:
        time.sleep(1)
        game = False