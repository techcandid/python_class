def register():
    account_name = input("enter Acount Name")
    process = True
    while process:
        pin = (int("enter 4 digit: "))
        if pin not in range (1000,10000):
            print("invalid Pin")
            print(f'please try again!')
        else:
            print("Registration Successful!")
            process = False
            return account_name, pin 
        

name, pin = register()
print(name)
print(pin)