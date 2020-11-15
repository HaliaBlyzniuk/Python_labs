from random import randint
n = int(input("Enter amount of figures in a list: "))
while n <= 0:
    n = int(input("Amount of figures can't be less than 0. Enter one more time: "))
numbers = []
count = 0
num_div = []
for i in range(n):
    x = randint(0,100)
    numbers.append(x)
    if x%3 == 0 or x%5 == 0:
        count+=1
        num_div.append(x)
print("Initial list is {}".format(numbers))
if count == 0:
    print ("There are no number that can be divided by 3 or 5.")
else:
    print ("There are {} figures that can be divided by 3 or 5".format(count))
    print("Final list is: {}".format(num_div))
