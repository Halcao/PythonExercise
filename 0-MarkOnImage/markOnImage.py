#-*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def get_format(name):
    arr = name.split('.')
    return name.replace('.'+arr[-1], '_new')+'.'+arr[-1]

def add_text(img, text, color, size):
    font = ImageFont.truetype('simsun.ttc', size)
    im = Image.open(img)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    draw.text((width - 40, 40), text, font=font, fill=color)
    im.save(get_format(img))

if __name__ == '__main__':
   add_text('./head.png', '250', "#ff0000", 30)
