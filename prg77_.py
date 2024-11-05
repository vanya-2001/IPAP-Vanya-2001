
import csv

with open('personal.csv') as f:
   # reader = csv.reader(f, delimiter=';', quotechar=('"'))
    #for index, row in enumerate(reader):
    #    print(row)
   reader = csv.DictReader(f, delimiter=';', quotechar=('"'))
   row = list(reader)
   for r in row:
       print(r['ФИО'])

    #print(list(reader))
    #print(list(reader))

#table = [r.split(';') for r in text.split('\n')]

#print(table[2][1])