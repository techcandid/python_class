import random
def group2():
    account_name = input("enter your user account name: ")
    password = int(input("enter password"))
    account_num = random.randint(100000000, 999999999)
    account_bal = 0.00

    print(f"account_name: {account_name}")
    print(f"password: {password}")
    print(f"account_num: {account_num}")
    print(f"account_bal: {account_bal}")


    return account_bal,account_name,password,account_num  
group2()