import pygame as pg
import random
import time

pg.init()
pg.font.init()

#Settings
winx = 450
winy = 450
FPS = 60

class Polje:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.number = random.randint(1, 3)
        self.secretColor = self.color

#Polja
mines = [[Polje(0,0, "light grey")],
         [Polje(0,50, "grey")],
         [Polje(0, 100, "light grey")],
         [Polje(0, 150, "grey")],
         [Polje(0, 200, "light grey")],
         [Polje(0, 250, "grey")],
         [Polje(0, 300, "light grey")],
         [Polje(0, 350, "grey")],
         [Polje(0, 400, "light grey")],
         ]

for i in range(len(mines)):
    for j in range(1, 10):
        if mines[i][j - 1].color == "light grey":
            mines[i].append(Polje(mines[i][j - 1].x + 50, mines[i][j - 1].y, "grey"))
        elif mines[i][j - 1].color == "grey":
            mines[i].append(Polje(mines[i][j - 1].x + 50, mines[i][j - 1].y, "light grey"))

bomb = random.randint(1, 50)
print(bomb//10, bomb%10)
mines[bomb//10 - 1][bomb % 10 - 1].secretColor = "red"            

#Display
display = pg.display.set_mode((winx, winy))

game = True
end = False

while game:
    #Clock
    pg.time.Clock().tick(FPS)

    display.fill("white")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mousePos = pg.mouse.get_pos()
            for i in mines:
                for j in i:
                    if mousePos[0] >= j.x and mousePos[0] <= j.x + 50 and mousePos[1] >= j.y and mousePos[1] <= j.y + 50:
                        print(f"Click {j.x, j.y}")
                        
                        if j.secretColor != "red":
                            j.color = "#7a7a7a"
                        else:
                            j.color = "red"
                            end = True
    for lane in mines:
        for mine in lane:
            pg.draw.rect(display, mine.color, (mine.x, mine.y, 50, 50))
    #Update
    pg.display.update()

    if end == True:
        time.sleep(1)
        game = False