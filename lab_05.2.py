line = input("Enter a string with latin letters: ")
while not line.isalpha():
    line = input("The string should contain only latin letters: ")
letters = {}
flag = 0
for i in range(len(line)):
    if line[i] not in letters:
        letters[line[i]] = line.count(line[i])
for letter,count in letters.items():
    if count > 1:
        print("Letter {} is in the line for {} times".format(letter,count))
        flag = 1
if not flag:
    print("There are no letters that repeat 2 times and more")


