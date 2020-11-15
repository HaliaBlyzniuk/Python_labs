text = input("Enter a text: ")
list = list(text)
print(list)
if text[0]=='0' or (ord(list[0])>64 and ord(list[0])< 123):
    print("The first number shoud not be 0!" )
else:
    num = int(text[0])
    if text[1:].isalpha():
        if num == len(text)-1:
            print("Text is correct. {} = number fo symbols after it({})".format(num,len(text)-1))
        else:
            print("The first number not equal to the number of letters")
    else:
        print("Not all symbols after {} are letters".format(num))
    
