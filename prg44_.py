# Справочная вокзала
trains = {
    '001А': ['"Красная стрела"', 'Москва - Санкт-Петербург', '23:55'],
    '025B': ['"Смена"', 'Москва - Воронеж', '20:47'],
}
#
while True:
    num = input('Введите номер поезда (или "стоп" для выхода): ').strip().upper()

    if num == 'СТОП' or num == 'CNJG':
        print('До следующих встреч!')
        break
    # num = input('Ведите номер поезда: ')
    if num not in trains.keys():
        print('Такого поезда нет в сообщении')
        for k, v in trains.items():
            print(f'{k} - {v[1]}')
    else:
        print(f'Поезд {num}, {trains[num][0]}, маршрут {trains[num][1]},'
                  f' отправляется {trains[num][2]}')
