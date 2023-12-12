print("""
      
     --- Welcome to the ATM ---   
      1. Check Balance
      2. Withdraw money
      3. Deposit money
      4. Quit -> Q
""")

check=1000

while True:
    select=input("Please select an option: ")

    if select=="1":
        print("Your balance is: ",check)
    elif select=="2":   
        withdraw=int(input("How much do you want to withdraw: "))
        if withdraw>check:
            print("You don't have enough money!")
        else:
            check-=withdraw
            print("Your balance is: ",check)
    elif select=="3":
        deposit=int(input("How much do you want to deposit: "))
        check+=deposit
        print("Your balance is: ",check)
    elif select=="Q":
        print("See you later!")
        break
    else:
        print("Please select a valid option!")
        continue
    
