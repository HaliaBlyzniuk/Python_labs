from random import randint
r = int(input("Введіть кількість рядків: "))
c = int(input("Введіть кількість стовпців: "))

matrix = []
suma = 0
for i in range(r):
    row = []
    for j in range(c):
        elem = randint(-10,10)
        row.append(elem)
        if i+j == c-1:
            suma+= elem
    matrix.append(row)

for row in matrix:
    for elem in row:
        print("%3d "%elem,end=" ")
    print("\n")
    
print("Сума елементів бічної діагоналі = {}".format(suma))

print()
    
