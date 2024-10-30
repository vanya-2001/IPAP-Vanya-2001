# Доп. библиотека PIL (pillow)
from PIL import ImageDraw, Image, ImageFont

# создаем и рисуем original.jpg
# холст
try:
    sky_canvas = Image.open('Sky.jpg')
except FileNotFoundError:
    print('Файл не найден')

crop = sky_canvas.crop((0, 0, 200, 200))
crop.save('sky_canvas.jpg')

sky_canvas = Image.open('sky_canvas.jpg')
# создаём рисовальщик
draw = ImageDraw.Draw(sky_canvas)

draw.rectangle((0, 0, 200, 200), fill=None, outline=(0, 0, 0), width=30)
draw.line((100, 0, 100, 200), fill=(0, 0, 0), width=30)
draw.line((0, 100, 200, 100), fill=(0, 0, 0), width=30)
# sky_canvas.save('sky_canvas_2.jpg')
# напишем текст
text_1 = 'Небо в клеточку'
font_txt = ImageFont.truetype(font='arial.ttf',  size=22)
draw.text( (22, 87), text_1, fill='red', font=font_txt, align='centered')
draw.circle((100,100), radius=90, fill= None, outline='green', width=3)
draw.ellipse((5, 50, 195, 150), outline='white', width=2)
sky_canvas.save('sky_canvas_txt.jpg')

"""
# создаем и рисуем original.jpg
# холст
canvas = Image.new("RGB", (200, 200), (255, 255, 255))

# создаём рисовальщик
draw = ImageDraw.Draw(canvas)

draw.line((0, 0, 200, 200), fill=(244, 0, 0), width=3)

# canvas.save('line.png', 'PNG')
# рисуем прямоугольник
draw.rectangle((0, 0, 50, 50), (0, 0, 255), outline=(255, 200, 100), width=4)

canvas.save('line_rest.png', 'PNG')
"""
"""
# рисуем полигон (треугольник)
draw.polygon(xy=
             ((200,200),
             (150,200),
             (200,150)), fill='red')
canvas.save('canvas_poli.jpg')
"""
