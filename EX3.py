import sys
import pygame as pg

from Class.Button import Button
from Class.Rectangle import Rectangle
from Class.InputBox import InputBox

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

# ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(win_x/2, 100, 140, 32, COLOR_INACTIVE,COLOR_ACTIVE,FONT,False)  # สร้าง InputBox1
input_box2 = InputBox(win_x/2, 200, 140, 32, COLOR_INACTIVE,COLOR_ACTIVE,FONT,False)  # สร้าง InputBox2
input_box3 = InputBox(win_x/2, 300, 140, 32, COLOR_INACTIVE,COLOR_ACTIVE,FONT,True)  # สร้าง InputBox3
# เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
input_boxes = [input_box1, input_box2, input_box3]
run = True

font = pg.font.Font(None, 32) #ตั้งค่าว่าเอา FONT อะไร

#Text ของตัว Nickname
textNick = font.render('NickName : ', True, pg.Color('black'), pg.Color('White'))
textNickRect = textNick.get_rect()
textNickRect.center = (int(win_x/2) - 100, 115)

#Text ของตัว Name
textName = font.render('Name : ', True, pg.Color('Black'), pg.Color('White'))
textNameRect = textName.get_rect()
textNameRect.center = (int(win_x/2) - 100, 215)

#Text ของตัว Age
textAge = font.render('Age : ', True, pg.Color('Black'), pg.Color('White'))
textAgeRect = textAge.get_rect()
textAgeRect.center = (int(win_x/2) - 100, 315)

#Text เปล่ารอรับค่า
textTemp = font.render('', True, pg.Color('Black'), pg.Color('White'))
textTempRect = textTemp.get_rect()
textTempRect.center = (int(win_x/2)-100, 415)

#สร้างปุ่ม
btn = Button(int(win_x/2)-50, 350, 100, 50,)

while run:
    screen.fill((255, 255, 255))
    btn.draw(screen)

    screen.blit(textNick, textNickRect)
    screen.blit(textName, textNameRect)
    screen.blit(textAge, textAgeRect)
    screen.blit(textTemp, textTempRect)

    # ถ้ากดเมาส์อยู่บนปุ่ม
    if btn.isMouseOn():
        # print("Mounse On")
        btn.color = pg.Color('Blue')
        #ถ้ากดปุ่มให้ทำงาน
        if btn.isMousePress():
            # print("Mouse Press")
            temp = "Hello {} {}! You are {} years old.".format(input_box1.text, input_box2.text, input_box3.text)
            textTemp = font.render(temp, True, pg.Color('Black'), pg.Color('White'))
            textTempRect = textTemp.get_rect()
            textTempRect.center = (int(win_x/2), 450)
    else:
        btn.color = pg.Color('red')

    for box in input_boxes:  # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update()  # เรียกใช้ฟังก์ชัน update() ของ InputBox
        # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        box.draw(screen)

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()
