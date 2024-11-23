# import pickle
import json

pets_info = {
    'pets': [
        {
            'pet': 'dog',
            'name': 'Reks',
            'food': 'Purina',
            'age': 4
        },
        {
            'pet': 'cat',
            'name': 'Matilda',
            'food': 'Whiskas',
            'age': 3
        }
    ]
}

# print(pets_info['pets'][1]['name'])
# сериализация  pickle
# with open ('data.pickle', 'wb') as f:
#     pickle.dump(pets_info, f)

# десериализация  pickle
# with open('data.pickle', 'rb') as f:
#     data = pickle.load(f)
# print(data)


# сериализация JSON
# with open ('pets.json', 'w') as f:
#     json.dump(pets_info, f)

# десериализация JSON
with open ('pets.json', 'r') as f:
    temp = json.load(f) #  temp = json.loads(f)
    # если строка с переменной и в этой переменной есть
    # json- файл,  то используем loads

print(temp)