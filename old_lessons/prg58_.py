# "Бросаемся" исключениями (throw (Java, C++, C#) -> raise)
min_val = 1
max_val = 10
try:
    cur_val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
    if not min_val <= cur_val <= max_val:
        raise ValueError('введенное число вне диапазона ({min_val}...{max_val}).')
    print(f'да, Число {cur_val} лежит в диапазоне от {min_val} до {max_val}')
 #   if not min_val <= cur_val <= max_val:
 #       raise ValueError('введенное число вне диапазона')
except ValueError as exp:
    print(f'надо быть повнимательнее:', exp)
