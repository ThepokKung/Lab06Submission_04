import sys 
import pygame as pg

# Class Start
from Class.Button import Button
# from Class.Rectangle import Rectangle
# from Class import Button

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
# firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    # firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด

    if btn.isMouseOn():
        btn.w = 200
        btn.h = 300
        btn.color=pg.Color('gray')
        if btn.isMousePress():
            btn.color = pg.Color('purple')
    else:
        btn.w = 100
        btn.h = 100
        btn.color = pg.Color('red')
    btn.draw(screen)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False