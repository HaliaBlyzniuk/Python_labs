# Варіанти 2, 6, 10, 14.  Знайти площу трикутника за трьома сторонами 𝑎, 𝑏, 𝑐. 
# Оформити перевірку вхідних даних (що трикутник з такими сторонами 𝑎, 𝑏, 𝑐 існує) 
# за допомогою оператора assert.
import math as m
while True:
    a = input("Enter lenght of the 1st side: ")
    try:
        a = int(a)
    except ValueError:
        print("You need to enter a number!")
    else:
        try:
            assert a > 0
        except AssertionError:
            print("The lenght can not be less than 0!")
        else:
            break
        

while True:
    b = input("Enter lenght of the 2nd side: ")
    try:
        b = int(b)
    except ValueError:
        print("You need to enter a number!")
    else:
        try:
            assert b > 0
        except AssertionError:
            print("The lenght can not be less than 0!")
        else:
            break
while True:
    c = input("Enter lenght of the 3rd side: ")
    try:
        c = int(c)
    except ValueError:
        print("You need to enter a number!")
    else:
        try:
            assert c > 0
        except AssertionError:
            print("The lenght can not be less than 0!")
        else:
            break

try:
    assert a+b>c and b+c>a and c+a>b
except AssertionError:
    print("The sum of two sides should be bigger than the third side!\nThe triangle does not exist!")
else:
    p = (a+b+c)/2
    s = m.sqrt(p*(p-a)*(p-b)*(p-c))
    print("The square of the triangle is {}".format(s))


