import configparser
import requests

config = configparser.ConfigParser()  # объект для обращения к ini

# читаем
config.read('settings.ini')

key = config['Weather']['key']

res = requests.get('http://api.openweathermap.org/data/2.5/find',
                   params={'q': 'Санкт Петербург',
                           'type': 'like',
                           'units': 'metric',
                           'APPID': key})

data = res.json()
#print(data)

# data = res.json()
#
temp = data['list'][0]['main']

print(f"Температура:, {temp['temp']} °C")
print(f'Ощущается как:', temp['feels_like'])
print(f'Давление:', temp['pressure'])
print(f'Влажность:', temp['humidity'])

"""
{'message': 'like', 'cod': '200', 'count': 2,
'list': [{'id': 498817, 'name': 'Saint Petersburg',
'coord': {'lat': 59.8944, 'lon': 30.2642},
'main': {'temp': 2.25, 'feels_like': -0.8,
'temp_min': 2.25, 'temp_max': 3.08, 'pressure': 1027,
'humidity': 95, 'sea_level': 1027, 'grnd_level': 1024},
'dt': 1731398948, 'wind': {'speed': 3, 'deg': 230},
'sys': {'country': 'RU'},
'rain': None, 'snow': None,
'clouds': {'all': 100},
'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'id': 536203, 'name': 'Saint Petersburg', 'coord': {'lat': 59.9167, 'lon': 30.25}, 'main': {'temp': 2.32, 'feels_like': -0.71, 'temp_min': 2.32, 'temp_max': 3.15, 'pressure': 1027, 'humidity': 95, 'sea_level': 1027, 'grnd_level': 1025}, 'dt': 1731398714, 'wind': {'speed': 3, 'deg': 230}, 'sys': {'country': 'RU'}, 'rain': None, 'snow': None, 'clouds': {'all': 100}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}
"""

"""
{'message': 'like', 'cod': '200', 'count': 2, 
'list': [ {
    'id': 498817, 
    'name': 'Saint Petersburg', 
    'coord': {
                'lat': 59.8944, 'lon': 30.2642}, 
                'main': {'temp': 0.03, 'feels_like': -5.88, 'temp_min': 0.03, 'temp_max': 0.08, 'pressure': 1008, 'humidity': 83, 'sea_level': 1008, 'grnd_level': 1005}, 
                'dt': 1732417747, 
                'wind': {'speed': 7, 'deg': 260}, 'sys': {'country': 'RU'}, 'rain': None, ' 100}, 
                'weasnow': {'1h': 0.1}, 'clouds': {'all':ther': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'id': 536203, 'name': 'Saint Petersburg', 'coord': {'lat': 59.9167, 'lon': 30.25}, 'main': {'temp': 0.1, 'feels_like': -5.79, 'temp_min': 0.1, 'temp_max': 0.15, 'pressure': 1008, 'humidity': 84, 'sea_level': 1008, 'grnd_level': 1006}, 'dt': 1732417513, 'wind': {'speed': 7, 'deg': 260}, 'sys': {'country': 'RU'}, 'rain': None, 'snow': {'1h': 0.1}, 'clouds': {'all': 100}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}
"""