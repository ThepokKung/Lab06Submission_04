import sys
import pygame as pg

from Class.Rectangle import Rectangle

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
        self.color = pg.Color('red')
        self.press_Color = pg.Color('purple')
        self.on_Color = pg.Color('gray')


    def isMouseOn(self):
        # mousePos =   #ดึง Pos ของ Mouse
        mouseX, mouseY = pg.mouse.get_pos()  #แยก PosX-PosY ของ Mouse

        if self.x <= mouseX <= self.x + self.w and self.y <= mouseY <= self.y + self.h:
            return True
        else:
            return False
    
    def isMousePress(self):
        mouseX, mouseY = pg.mouse.get_pos()  #แยก PosX-PosY ของ Mouse

        if self.x <= mouseX <= self.x + self.w and self.y <= mouseY <= self.y + self.h:
            if pg.mouse.get_pressed()[0] == 1:
                return True
        return False

    def draw(self, screen):
        if self.isMouseOn():
            pg.draw.rect(screen,self.on_Color,(self.x,self.y,self.w,self.h))
            if self.isMousePress():
                 pg.draw.rect(screen,self.press_Color,(self.x,self.y,self.w,self.h))
        else:
             pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
    