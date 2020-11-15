error = "You've entered incorrect value. Try one more time:"

x = float(input("Enter x : "))
e = float(input("Enter e > 0: "))   
while e < 0:
    print (error)
    
    e = float(input("Enter  e > 0: "))

old_a = x
a = (2*old_a) + ((16+x)/(4+abs(old_a**3)))
n = 2
while abs(a - old_a) >= e and n <= 100:
    old_a = a
    a = (2*old_a) + ((16+x)/(4+abs(old_a**3)))
    n += 1
    print(old_a,a)
if n > 100:
    print("There is no proper element")
else:
    print("Element a{} = {} is the first proper element".format(n,a))
    print("a{} - a{} = {}".format(n,n-1,a-old_a))
