from random import random
from random import choice
names = ['Lilly', 'James', 'Ronald', 'Hugrid', 'Jane', 'Severus', 'Harry', 'Hermiona', 'Tom']
surname = ['Potter', 'Whizly', 'Granger', 'Love', 'Snag', 'Collinz', 'Malfoy', 'Reddle']
students = {}

n = int(input("Enter nuber of students: "))
for i in range(n):
    name = choice(names)+" "+choice(surname)
    studID = choice(name).upper() + choice(name).upper()
    for i in range(8):
        studID+=str((round(random()*10)))
    marks = []
    for i in range (5):
        marks.append(round(random()*100))
    students[studID] = [name, round(1+ random()*5),marks]
    
for key,val in students.items():
    print("{} : {}".format(key,val))

average_point = {}

