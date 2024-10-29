# Доп. библиотека PIL (pillow)
from PIL import ImageDraw, Image

# создаем и рисуем original.jpg
# холст
canvas = Image.new("RGB", (200, 200), (255, 255, 255))

# создаём рисовальщик
draw = ImageDraw.Draw(canvas)

draw.line((0, 0, 200,200), fill=(244,0,0), width=3)

canvas.save('line.png', 'PNG')
