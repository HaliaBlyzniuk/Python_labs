import random
n = int(input("Enter how many students are in university: "))
languages = ["English", "Spanish", "France", "German", "Chineese", "Russian",
             "Polish", "Japaneese", "Italian"]
names = ("Julia", "Serhiy", "Max", "Kristi", "Helen", "Mary", "Jane", "Khloe")
surnames = ("Smith", "Johnsons", "White", "Black", "Swan", "Potter", "Whizly", "Granger")
students = {}
repeat = []
for i in range (n):
    name = random.choice(names) +" " + random.choice(surnames)
    lang = set(random.choices(languages,k = random.randrange(6,len(languages))))
    repeat +=lang
    students[name] = lang

for name,lang in students.items():
    print(name, " : ", lang)

al_lang = []
for i in range(len(repeat)):
    if repeat.count(repeat[i])==n:
        if repeat[i] not in al_lang:
            al_lang.append(repeat[i])
if len(al_lang)==0:
    print("There are no common languages among all students.")
else:
    print("All students learn {}".format(al_lang))
        
    

