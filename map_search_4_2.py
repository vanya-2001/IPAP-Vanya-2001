from urllib.request import urlopen
from urllib.parse import urlencode
import xml.etree.ElementTree as et
 
 
# пока пустой перечень параметров запроса
data = {}
# API-ключ
data['apikey'] = '40d1649f-0493-4b70-98ba-98533de7710b'
# адрес для поиска на карте
data['geocode'] = 'СПб, Можайская, 2'
 
# основная часть ссылки для обращения к геокодеру
url = 'http://geocode-maps.yandex.ru/1.x/'
 
# преобразуем набор параметров в формат URL
url_values = urlencode(data)
# формируем полную ссылку
full_url = '?'.join([url, url_values])
# получаем ответ по ссылке
response = urlopen(full_url)
 
# полученный ответ преобразуем в XML-формат
res = response.read().decode('UTF-8')
 
# начинаем расшифровывать XML
root = et.fromstring(res)
# "вытаскиваем" координаты
coords = root.find('.//{http://www.opengis.net/gml}pos').text
 
# координаты в консоль уже не выводим
# вновь пустой перечень параметров запроса
map_data = {}
# добавляем в запрос все необходимые параметры:
# широту и долготу
map_data['ll'] = coords.replace(' ', ',')
# протяжённость области поиска 
map_data['spn'] = ','.join(['0.0025', '0.0025'])
# отображаем карту
map_data['l'] = 'map'
# добавим значок на карту
map_data['pt'] = coords.replace(' ', ',') + ',pm2dgl'
 
# основная часть ссылки для обращения к
# статическому контенту Яндекс-карт
map_url = 'http://static-maps.yandex.ru/1.x/'
 
# преобразуем набор параметров в формат URL
url_values = urlencode(map_data)
# формируем полную ссылку
full_url = '?'.join([map_url, url_values])
print(full_url)
