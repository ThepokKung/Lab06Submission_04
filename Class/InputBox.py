import pygame as pg


class InputBox:

    #เพิ่มตัวแปรขึ้นมา 
    def __init__(self, x, y, w, h, color_inactiveas, color_active, font, isdigi , text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color_inactive = color_inactiveas
        self.color_active = color_active
        self.color = color_inactiveas
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.isdigi = isdigi #ตัวแปรที่ทำการเช็คว่ารับแค่ INT ใช่ไหม

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # เปลี่ยนสีของ InputBox
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # เพิ่มทำการเช็คว่า ถ้าเปิด isdigi = True ให้ดูว่าตัวที่พิมพ์มาเป็นตัวเลขไหม ถ้าใช่ค่อยเพิ่มเข้าไป
                    if self.isdigi == True:
                        if chr(event.key).isnumeric(): #คำสั่งเช็คว่าตัวที่กดเป็นตัวเลขไหม
                            self.text += event.unicode
                    else:
                        self.text += event.unicode      
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
