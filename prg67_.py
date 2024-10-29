# Доп. библиотека PIL (pillow)
from PIL import Image, ImageFilter, ImageDraw

# пробуем прочитать файли
try:
    orig = Image.open('original.jpg')
except FileNotFoundError:
    print('Файл не найден')

print('Парамаетры файла')
print(f'Формат {orig.format}')
print(f'Размеры {orig.size}')
print(f'Цветовая схема {orig.mode}')

w, h = orig.size  # получили и распаковали кортеж
pixels = orig.load()  # список пикселей : ряд место строув - [x, y}


"""
for x in range(w):
    for y in range(h):
        r, g, b = pixels[x, y]  # получили и распаковали кортеж
        pixels[x, y] = b, g, r

orig.save('inverted.jpg')

for x in range(w):
    for y in range(h):
        r, g, b = pixels[x, y]  # получили и распаковали кортеж
        average = (r + g + b) // 3
        pixels[x, y] = average, average, average

orig.save('grayscale.jpg')
"""


# blur = orig.filter(ImageFilter.BLUR)
# blur.save('blur.jpg')
# blur_g = orig.filter(ImageFilter.GaussianBlur(10))
# blur_g.save('blur_g.jpg')

# crop = orig.crop((140, 35, 460, 365))
# crop.save('crop.jpg')

contour = orig.filter(ImageFilter.CONTOUR)
contour.save('contour.jpg')
