# Сложное  условие ДОГИЧЕСКОЕ "И"
# когда должны соблюдаться несколько условий одновременоо
# МЛМ ... ИЛИ... МЛМ .. без ограничений,
# Программа которая правильгно здоровается
# формализация задачи
#  6 <= hour < 12 Доброе утро
#  12 <= hour < 17 Добрый день
#  18 <= hour < 22 Добрый дечер
#  доброй ночи


hour = 19

"""
# Первый способ Классический способ записи сложного условия
if hour >= 6 and hour < 12: # При составном условии AND является логческим "И",
    # то есть когда условия ДОЛЖНЫ быть выполнены и слева и СПРАВА, == TRUE
    # если хотябы одно из условий не выполняется возвращается Fakse
    # pass    # идем дальше
    print('Доброе утро!')
elif hour >= 12 and hour < 18:
    print('Добрый день!')
elif hour >= 18 and hour < 22:
    print('Добрый вечер!')
else:
    print('Доброй ноыи!')
"""

# Второй способ # simplyfy
if 6 <= hour < 12: # При составном условии AND является логческим "И",
    # то есть когда условия ДОЛЖНЫ быть выполнены и слева и СПРАВА, == TRUE
    # если хотябы одно из условий не выполняется возвращается Fakse
    # pass    # идем дальше
    print('Доброе утро!')
elif 12 <= hour < 18:
    print('Добрый день!')
elif 18 <= hour < 22:
    print('Добрый вечер!')
else:
    print('Доброй ноыи!')