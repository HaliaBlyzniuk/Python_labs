print("Program counts f = max(y-x,x+y,1+x)")
x = float(input ("Enter x: "))
y = float(input ("Enter y: "))

if (y-x > x+y and y-x > 1+x):
    max = y-x
    str = 'y-x'
elif (x+y > y-x and x+y > 1+x):
    max = x+y
    str = 'x+y'
else:
    max = 1+x
    str = '1+x'

print ("Maximum is ", str ," = ",max)
