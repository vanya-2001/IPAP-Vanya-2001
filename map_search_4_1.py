from urllib.request import urlopen
from urllib.parse import urlencode
import xml.etree.ElementTree as et
 
 
# пока пустой перечень параметров запроса
data = {}
# API-ключ
data['apikey'] = '40d1649f-0493-4b70-98ba-98533de7710b'
# адрес для поиска на карте
data['geocode'] = 'СПб, Можайская, 2'
 
# обращение к геокодеру
url = 'http://geocode-maps.yandex.ru/1.x/'
 
# преобразуем набор параметров в формат URL
url_values = urlencode(data)
# формируем полную ссылку
full_url = '?'.join([url, url_values])
# получаем ответ по ссылке
response = urlopen(full_url)
 
# полученный ответ в XML преобразуем в UTF-8 формат
res = response.read().decode('UTF-8')
 
# начинаем расшифровывать результат - XML
root = et.fromstring(res)
# "вытаскиваем" координаты
coords = root.find('.//{http://www.opengis.net/gml}pos').text
# выводим координаты к консоль
print(coords)
