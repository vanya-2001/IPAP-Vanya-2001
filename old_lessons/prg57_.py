#def Circus():
while True:
    try:
        int_val = int(input('Ведите целое число: '))
        print(f'Ура! Вы ввели число {int_val}')
        break
    except ValueError:
        print('Ну просили же Вас, ввести Ц Е Л О Е число!')
        print('Попробуйте снова')





