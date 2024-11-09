# Доп. библиотека PIL (pillow)
from PIL import ImageDraw, Image

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

draw.rectangle((0, 0, 200, 200), fill=None, outline=(0, 0, 0), width=10)
draw.line((100,0, 100,200), fill=(0, 0, 0), width=10)
draw.line((0,100, 200,100), fill=(0, 0, 0), width=10)
sky_canvas.save('sky_canvas_2.jpg')


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
