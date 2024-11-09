# Управляющая последовательность строк
# Escape sequence
# / - slash
#  \ - backslash  - начало управляющей последовательность
# \n - перевод на другую строку ТОЛЬКО ВНУТРИ СТРОКИ
# \t - табулято
# \\ - экранирование backslash особенно в прописании путей path

# string = 'Привет\nучастникам\nсоревнований!'
# path = 'c:\\windows\\com.exe'
# print(string)
# print(path)

# confilct = "Кафе "Аист"" # wrong неправильно
#     confilct = "Кафе "Аист""
#                       ^^^^
# SyntaxError: invalid syntax
confilct = "Кафе \"Аист\"" # correct Правильно

print(confilct)