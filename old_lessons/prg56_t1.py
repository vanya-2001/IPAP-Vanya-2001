#def Circus():
while True:
    try:
        int_val = int(input('Ведите целое число: '))
        print(f'Вы ввели число {int_val}')
        break
    except ValueError:
        print('Вас просили ввести число')
        print('Попробуйте снова')





