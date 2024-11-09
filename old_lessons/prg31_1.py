# Функции chr ord
# ASCII (256)
# INICOD (65536)
# """
# print(ord('a'))
#
# print(chr(171))
# print(chr(181))
# print(f'{chr(171)}Привет!{chr(187)}')
# # \x означает что мы хотим напечатать символ в 16-чной кодировке ASCII
# # \xB0 = chr(176)
# print('75' + chr(176) + 'C')
# print(f'75{chr(176)}C')
# print('75\xB0C') # hex ASCII
# print('\u2710') # uniCode
# """

import string as s

temp = s.digits + s.ascii_lowercase + s.ascii_uppercase
m_set = set(temp) - {'l', 'O', 'I', '1', '0'}
print(m_set)
