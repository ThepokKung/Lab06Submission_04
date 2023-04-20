import sys
import pygame as pg

from Class.Button import Button
from Class.Rectangle import Rectangle


class InputBox:

    def __init__(self, x, y, w, h,  isdigi, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.isdigi = isdigi

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.isdigi is True:
                        self.text += event.unicode
                    else:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

# ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(win_x/2, 100, 140, 32, True)  # สร้าง InputBox1
input_box2 = InputBox(win_x/2, 200, 140, 32, True)  # สร้าง InputBox2
input_box3 = InputBox(win_x/2, 300, 140, 32, False)  # สร้าง InputBox3
# เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
input_boxes = [input_box1, input_box2, input_box3]
run = True

font = pg.font.Font(None, 32)
textNick = font.render('NickName : ', True,
                       pg.Color('black'), pg.Color('White'))
textNickRect = textNick.get_rect()
textNickRect.center = (int(win_x/2) - 100, 115)

textName = font.render('Name : ', True, pg.Color('Black'), pg.Color('White'))
textNameRect = textName.get_rect()
textNameRect.center = (int(win_x/2) - 100, 215)

textAge = font.render('Age : ', True, pg.Color('Black'), pg.Color('White'))
textAgeRect = textAge.get_rect()
textAgeRect.center = (int(win_x/2) - 100, 315)

textTemp = font.render('', True, pg.Color('Black'), pg.Color('White'))
textTempRect = textTemp.get_rect()
textTempRect.center = (int(win_x/2)-100, 415)

btn = Button(int(win_x/2)-50, 350, 100, 50,)

while run:
    screen.fill((255, 255, 255))
    btn.draw(screen)

    screen.blit(textNick, textNickRect)
    screen.blit(textName, textNameRect)
    screen.blit(textAge, textAgeRect)
    screen.blit(textTemp, textTempRect)

    if btn.isMouseOn():
        # print("Mounse On")
        btn.color = pg.Color('Blue')
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
