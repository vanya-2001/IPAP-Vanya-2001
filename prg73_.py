# Syntax Sugar (синтаксический сахар)
# Списочные выражения list comprehensions
# [ выражение for  переменная in  источник  if  условие]


# a =[ i for i in range(1,11)]
#ipaddress = '192.168.0.1'

greet = 'Hello World'

c = [i for i in greet if i.isupper()]
print(c)

d = [(pos, char) for pos, char in enumerate(greet)]
print(d)


# a =map(int, s)
# s = ipaddress.split('.')
# a = [int(i) for i in ipaddress.split('.') if int(i) > 0]
# b = [i for i in range(2, 12) if i % 2 == 0]
#b = [i for i in range(2, 11, 2)]
#print(b)
# a =[ i * i for i in range(1,11)]


# print(list(a))
# lambda a,b: a+b
