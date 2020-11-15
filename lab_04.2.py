text = input("Enter some text: ")
word = input("Enter a word: ")
for c in word:
    if (text.find(c)!=-1):
        print("Letter {} is in the text".format(c))
else:
    print("There are no coomon letters in the text")

