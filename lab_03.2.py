from random import random
import math as m
n = int(input("Enter the number of elements in the vector: "))
while (n<=0):
    n = int(input("Incorrect value! Try one more time : "))
vect = []
len_v = 0

print ("Random vector is: (", end = " ")
for i in range (n):
    vect.append(random()*10)
    len_v += pow(vect[i],2)
    print("{:.4}".format(vect[i]), end = ", ")
print (")")    
len_v = m.sqrt(len_v)
print ("\nThe length of the vector is {:.4f}".format(len_v))
