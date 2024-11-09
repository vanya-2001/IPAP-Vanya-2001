# Умный словарь, сохраненный в файл

d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple',
}
fo = open('clever.dict', 'wt', encoding='utf8')

fo.close()

# rus = ''
rus = input('Введите слово на русском для перевода (или "стоп" для выхода): ').strip().lower()

while rus != 'стоп' and rus != 'cnjg':
    if rus in d:
        print(f'Слово "{rus}" переводится как "{d[rus]}"')
    else:
        print(f'К сожалению, я не знаю перевода слова "{rus}"')
        new_word = input(f'А как слово "{rus}" переводится: ')
        d[rus] = new_word
        print(f'Теперь я знаю перевод слова "{rus}". Это - "{d[rus]}"')

    rus = input('Введите слово на русском для перевода (или "стоп" для выхода): ').strip().lower()

print('Приятно было пообщаться!')
