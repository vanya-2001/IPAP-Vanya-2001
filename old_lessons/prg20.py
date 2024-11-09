# string = "ТМ"
#  число элементов итерируемого объекта
number = input("Введите целое число: ")
length = len(number)
print('Число ', number, str(length) + "-х", "значное" )

print()


# total = 0
#
# for item in number:
#     total += int(item)
#
# print('Сумма разрядов числа',number, "равна",  total)
#
number = input("Введите целое число: ")
length = len(number)
print('Число ', number, str(length) + "-х", "значное" )

print()


total = 1

for item in number:
    total *= int(item)

print('Произведение разрядов числа',number, "равна",  total)

# for i in range(5):
#     pass # TODO
#     print('helloo')
#
# for _ in range(5):
#     print("Привет")