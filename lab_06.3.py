# До програми з клавіатури надходить послідовність цифр. Послідовність задається доти,
#  доки користувач не введе слово «досить». Слід зауважити, що користувач не є 
#  дисциплінованим і може замість цифр вводити будь-що. Якщо користувач вводить з 
#  клавіатури число більше за 9, то програма ініціює виключення RuntimeError. Якщо 
#  користувач вводить число менше за 0, то програма ініціює виключення TypeError. 
#  Якщо користувач вводить дійсне значення з діапазону від 0 до 9, то програма ініціює 
#  виключення ValueError. Підрахувати  кількість виключень кожного типу, що виникають
#  у програмі.

print("Введіть 'досить',щоб завершити")
runTime  = 0
typeError = 0
valError = 0

while True:
    x = input("Введіть цифру: ")
    if x =="stop":
        break
    else:
        try:
            x = int(x)
        except ValueError:
            print("Потрібно ввести цифру!")
            continue
        else:
            try:
                if x>9:
                    raise RuntimeError
            except RuntimeError:
                print("Ви ввели число більше за 9!")
                runTime+=1
            else:
                try:
                    if  x<0:
                        raise TypeError
                except TypeError:
                    print("Ви ввели число меше за 0!")
                    typeError+=1
                else:
                    try:
                        raise ValueError
                    except ValueError:
                        print("Ви ввели цифру від 0 до 9!")
                        valError+=1

print("Всього помилок:\n")
print("ValueError: {}\nRuntimeError: {}\n TypeError: {}".format(valError,runTime,typeError))


