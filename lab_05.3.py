from random import randint
seasons = { 'winter' : ('December', 'January', 'February'),
            'spring' : ('March', 'April', 'May'),
            'summer' : ('June', 'July', 'August'),
            'autumn' : ('September', 'October', 'November')
            }
statistics = {}
for val in seasons.values():
    for month in val:
        statistics[month] = randint(0,400)
for key,val in statistics.items():
    print("The average falls in {} is {} mm".format(key,val))
print()

for season in seasons:
    print ("The average ammount of fall-outs in {} is:\n(".format(season),end = " ")
    fall = 0
    for mon in seasons[season]:
        fall += int(statistics[mon])
        print(int(statistics[mon])," + ", end = " ")
    average = int(fall/3)
    print(")\\3 = ", average, "mm.")
    seasons[season] = seasons[season]+(average,)
    
print()
    
for key,val in seasons.items():
    print("{} : {}".format(key,val))

m = 10000
dry = "winter"
for key in seasons:
    for item in seasons[key]:
        if str(item).isnumeric():
            if item < m:
                m = item
                dry = key
    
print("{} is the most dry season : {} mm of fall-outs".format(dry.capitalize(),m))
