master_pwd = input("What is the master password? ")

def view():
    with open("passwords.txt",'r') as v:
        for line in v:
            print(line.rstrip())
    
def add():
    name = input("Enter user name: ")
    pwd = input("Enter user password: ")
    with open("passwords.txt",'a') as ps:
        ps.write(name + "|" + pwd + "\n")
while True:    
    ask = input("Do you want to add password or view passwords?(q to quit) ")
    if ask == "q":
        break
    if ask == "view":
        confirm = input("confirm the master password: ")
        if confirm == master_pwd:
            view()
        else:
            print("Wrong password!!!")
            break
    if ask == "add":
        add()