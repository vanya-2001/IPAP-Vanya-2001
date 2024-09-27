# Операции над множествами
a = {1, 2, 3, 4}
b = {2, 3, 5, 7, 11}

# 1 объединение множеств (union)
# result = a.union(b)
# print(result)

# # 2 объединение множеств (union)
# result = a | b # |  - "или"
# print(result)

# 2 пересечение множеств (intersection)
# result = a.intersection(b)
# result = a & b # &


# разность множества
# result = a.difference(b) # 'элементы входящие в a но не входящие в b
# result = a - b
# result = b - a
# print(result)

# симметричноая разность 'сумма множеств но с выбрасыванием элементов повтора
# элементы входящие в а
# result = a.symmetric_difference(b)
result = a ^ b
print(result)
