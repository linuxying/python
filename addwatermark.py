#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from PIL import Image, ImageDraw, ImageFont

# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 13)


# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text, font=font):
    rgba_image = image.convert('RGBA')
    # text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    text_overlay = Image.new('RGBA', rgba_image.size)
    image_draw = ImageDraw.Draw(text_overlay)

    # text_size_x, text_size_y = image_draw.textsize(text, font=font)
    for i in range(1, w, 60):
        for n in range(1, h, 13):
            text_size_x = w - i
            text_size_y = h - n
            # 设置文本文字位置
            print(rgba_image)
            text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)
            # 设置文本颜色和透明度
            image_draw.text(text_xy, text, font=font, fill=('#383838'))
            image_with_text = Image.alpha_composite(rgba_image, text_overlay)
    return image_with_text


def ranChar():
    # 随机字母
    checkcode = ''
    for i in range(5):
        current = random.randrange(0, 4)
        if current == i:
            tmp = chr(random.randint(65, 90))
        else:
            tmp = random.randint(0, 9)
        checkcode += str(tmp) + ' '
    return checkcode

im_before = Image.open("1.jpg")
w, h = im_before.size
# im_before.show()
im_after = add_text_to_image(im_before, ranChar())
im_after.show()
im_after.save('im_after.jpg')
