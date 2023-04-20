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

# Start Stauts
is_key_d_down = False
is_key_a_down = False
is_key_w_down = False
is_key_s_down = False

while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        # Start D key
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D down")
            is_key_d_down = True
        if event.type == pg.KEYUP and event.key == pg.K_d: 
            print("Key D up")
            is_key_d_down = False

        # Start A key
        if event.type == pg.KEYDOWN and event.key == pg.K_a: 
            print("Key A down")
            is_key_a_down = True
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A up")
            is_key_a_down = False

        #Start W key
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            print("Key W down")
            is_key_w_down = True
        if event.type == pg.KEYUP and event.key == pg.K_w:
            print("Key W up")
            is_key_w_down = False

        # Start S key
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            print("key S down")
            is_key_s_down = True
        if event.type == pg.KEYUP and event.key == pg.K_s:
            print("Key S up")
            is_key_s_down = False

    # Start Key manager
    if is_key_d_down:
        btn.x += 1
    if is_key_s_down:
        btn.y += 1
    if is_key_a_down:
        btn.x -= 1
    if is_key_w_down:
        btn.y -= 1