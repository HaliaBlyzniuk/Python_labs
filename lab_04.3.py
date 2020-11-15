mail = input("Enter your email address: ")
if mail.count("@") ==1 :
        check = mail.split("@")
        if "." in check[-1]:
            check = check[-1].split(".")
            if len(check[-1])< 2 or len(check[0])<4:
                print("Not enough characters after a dot!")
            else:
                print ("Email is correct")
        else:
            print("No dot '.' symbol in the email")
else:
    print("Invalid email")
