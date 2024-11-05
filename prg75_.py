# Регулярные выражения
# r - raw
# greedy minor

import re  # regular expression (  поиск по образцу)

#pattern = '20'
#pattern = r'\b\w{5}\b' # слова из 5 букв
#pattern = r'\+7\d{10}'
#pattern2 = r'[0-5][0-9]'
#pattern ='<img.*?>'
pattern = '<img[^>]+src=([^">]+)"'
t_string = 'Картинка <img src = "bg.jpg"> в тексте </p>'
#test_string = 'Google phone +71234567890'
#test_string = '10 плюс 20000 равно 40'
#result = re.search(pattern, test_string)
result = re.findall(pattern, t_string)
#string = r'C:\\Programm\word.exe'
print(result)