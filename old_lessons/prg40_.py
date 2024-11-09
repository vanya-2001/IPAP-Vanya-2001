# Операции между кортежами и другими объектами
# s = 'Python'
#
# res = sorted(s.lower())
# print(res)
# s = (255, 128, 64)
# res = sorted(s)
# print(res)

# Функция sorted() сортирует итерируемую последовательность
# и возвращает в виде списка

lst = ['бремя', 'время', 'стремя']
# print(sorted(lst))

temp = list(enumerate(lst))
print(temp)

for item in enumerate(lst):
    print(item)

for index, value in enumerate(lst):
    print(f' \n индекс - {index}, значение - {value}')


print('Существительные:')
for index, value in enumerate(lst):
    print(f'\t{index + 1}. {value}')
