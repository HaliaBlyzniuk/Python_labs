import math 

error = "You've entered incorrect value. Try one more time:"

a = float(input("Enter a !=0:  "))
while a == 0:
    print (error)
    a = float(input("Enter a !=0:  "))
x = float(input("Enter x != 0: "))
while x == 0:
    print (error)
    x = float(input("Enter x != 0: "))
e = float(input("Enter e > 0: "))   
while e < 0:
    print (error)
    e = float(input("Enter  e > 0: "))

prev_dod = 0.5
suma = prev_dod
k = 1
step =  (math.log(a+x))**(2*k)
dva = 2**(k)
fact = k
dod = step / (dva + fact)
print("The %d item is %f" %(k, prev_dod))
while abs(dod-prev_dod) >= e:
    print("The %d item is %f" %(k+1, dod))
    suma += dod
    prev_dod = dod
    k+=1
    step = (math.log(a+x))**(2*k)
    dva = 2**(k)
    fact *= k
    dod = step / (dva + fact)
    
print("The %dth item is odd %f" %(k+1, dod))
if k == 1 :
    sum = dod
print ("The sum is %f " %suma)
print ("There are %d items" %(k))
    
    
