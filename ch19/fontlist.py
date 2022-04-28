#! python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = r'C:\Windows\Fonts'
EXAMPLE = '愛Uniqフォント'
FONT_SIZE = 20
STEP = FONT_SIZE * 2 + 8

fonts = ['msmincho.ttc', 'msgothic.ttc', 'meiryo.ttc', 'YuGothB.ttc', 'YuGothL.ttc',
         'YuGothM.ttc', 'YuGothR.ttc', 'yumin.ttf', 'yumindb.ttf', 'yuminl.ttf',
         'UDDigiKyokashoN-B.ttc', 'UDDigiKyokashoN-R.ttc']
#for fname in os.listdir(FONT_DIR):
#    if fname.endswith('.ttf') or fname.endswith('.ttc'):
#        fonts.append(fname)

im = Image.new('RGBA', (1000, len(fonts) * STEP), 'white')
draw = ImageDraw.Draw(im)

y = 0
for font in fonts:
    draw.text((0, y), font, fill='red')
    for i in range(0, 4):
        try:
            f = ImageFont.truetype(font, FONT_SIZE, index=i)
            name = ' '.join(f.getname())
            x = 200 + 200 * i
            draw.text((x, y), name, fill='red')
            draw.text((x, y + FONT_SIZE), EXAMPLE, fill='black', font=f)
        except:
            pass
    y += STEP
    draw.line(((0, y), (1000, y)), fill='black')
        
im.save('fontlist.png')
