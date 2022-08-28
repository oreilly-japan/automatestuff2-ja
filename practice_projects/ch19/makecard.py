# 演習プロジェクト 19.7.3 座席カード

from PIL import Image, ImageDraw, ImageFont

CARD_WIDTH = 360
CARD_HEIGHT = 288

flower_im = Image.open('flower.png')

guest_file = open('guests.txt', 'r', encoding='utf-8')

for n,guest in enumerate(guest_file):
    guest = guest.strip()
    if guest == '':
        continue

    # 新しく画像を生成する
    im = Image.new('RGBA', (CARD_WIDTH, CARD_HEIGHT), 'white')

    # 画像を貼り付ける
    im.paste(flower_im, (0, 0), flower_im)

    draw = ImageDraw.Draw(im)
    # 名前を描く
    arial = ImageFont.truetype('meiryo.ttc', 32, index=0)
    tw, th = arial.getsize(guest)
    draw.text(((CARD_WIDTH - tw) / 2, (CARD_HEIGHT - th) / 2),
              guest, fill='black', font=arial)

    # 枠を描く
    draw.rectangle((0, 0, CARD_WIDTH - 1, CARD_HEIGHT - 1), outline='black')

    im.save('card{}.png'.format(n))

