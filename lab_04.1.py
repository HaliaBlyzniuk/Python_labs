for i in range (ord('A'),ord('X')+1):
    print ("{}{} ".format(chr(i),chr(i+32)), end = " ")
    if (i%8==0):
        print(end = "\n")
