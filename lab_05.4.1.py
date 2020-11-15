from random import random
from random import choice
names = ['Lilly', 'James', 'Ronald', 'Hugrid', 'Jane', 'Severus', 'Harry', 'Hermiona', 'Tom']
surnames = ['Potter', 'Whizly', 'Granger', 'Love', 'Snape', 'Collinz', 'Malfoy', 'Reddle']
students = {}

n = int(input("Enter nuber of students: "))
for i in range(n):
    studName =  choice(names)+" "+choice(surnames)
    studID = choice(studName).upper() + choice(studName).upper()
    for i in range(8):
        studID+=str((round(random()*10)))
    marks = []
    for i in range (5):
        marks.append(round(50+ random()*50))
    students[studID] = {}
    students[studID]['name'] = studName
    students[studID]['marks'] = marks;
    students[studID]['year'] = round(1+ random()*5)

print("\nThe list of students:\n")
for key,val in students.items():
    print("{} : {}".format(key,val))

all_marks = {}
for student in students:
    for key,data in students[student].items():
        if key == 'year':
            if data not in all_marks.keys():
                all_marks[data]= []
            all_marks[data]+=students[student]['marks']
print("\nMarks on each course are: ")
for key,val in all_marks.items():
    print("{} year : {}".format(key,val))

print("\nAverage marks on each course are:")
for key,val in all_marks.items():
    average = 0
    for i in val:
        average +=i
    average/=len(val)
    print("{} course : {}".format(key,average))

