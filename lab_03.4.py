import random
tup1 = ()
for i in range(10):
    tup1 =  tup1 + (round(random.random()*5),)
print("Кортеж 1: {}".format(tup1))

tup2 = ()
for i in range(10):
    tup2 =  tup2 + (round(random.random()*(-5)),)
print("Кортеж 2: {}".format(tup2))


tup3 = tup1+tup2

print("Кортеж 3: {}".format(tup3))

end = "нул"
if tup3.count(0)== 1 or  tup3.count(0) %10 == 1:
    end+="ь"
elif (tup3.count(0)>1 and tup3.count(0)<5) or (tup3.count(0)%10>1 and tup3.count(0)%10<5):
    end+="і"
else :
    end+="ів"
print ("Всьо у кортежі {} {}".format(tup3.count(0), end))

print()
