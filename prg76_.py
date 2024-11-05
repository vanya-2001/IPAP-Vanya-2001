# a = [[1,2,3],[3,4,5],[7,9,9]]
# print(a[2][1])

#a = [[x for x in range(i, 13, 4)] for i in range(1, 5)]
##print(a)

with open('personal.csv') as f:
    text = f.read()

table = [r.split(';') for r in text.split('\n')]

print(table[2][1])