while True:
    email = input("EmailId:").lower()
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email):
                if (email.count("@")==1):
                    if (email[-4] == ".") ^ (email[-3] == "."):
                        break
                    else:
                        print("Not a valid email5")
                else:
                    print("Not a valid email4")
            else:
                print("Not a valid email3")
        else:
            print("Not a valid email2")
    else:
        print("Not a valid email1")
print("Password must contain more than 6 letters")
while True:
    pwd = input("Password:")
    if len(pwd) >= 6:
        if pwd.isalpha():
            print("password must contain some numbers or digits")
        else:
            break
    else:
        print("password too short")