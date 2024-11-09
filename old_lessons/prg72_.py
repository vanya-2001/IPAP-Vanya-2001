# Syntax Sugar (синтаксический сахар)
# функция высшего порядка filter
users = [
    {'namr': 'Igor', 'age': 25},
    {'namr': 'Vova', 'age': 5} ,
    {'namr': 'Matew', 'age': 16},
    {'namr': 'Ivan', 'age': 11}

]

filtered_users = filter(lambda u: 6 < u['age'] < 11, users)

print(list (filtered_users))
#lambda a,b: a+b