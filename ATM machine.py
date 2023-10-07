import datetime
import time

print('''Welcome to ATM
         As this is mini ATM
          Plz user USERID - 12345
          Password - hellopython
          to get access to ATM''')
Amount=10000

def authenticate():
    userID=input("Enter the user(plz go through above message for ID and password)")
    password=input("Enter the password")
    if(userID=='12345' and password=='hellopython'):
        print("Authentication successfull")

        return True
    else:
        print("invalid credentials")
        return False


transaction_history=[]

def Withdrawl():
    global Amount
    print("You have selected the withdrawl option")
    withdrawl_amount=int(input("Enter the amount you want to withdraw"))
    if withdrawl_amount > Amount:
        print("Insufficient balance")
    else:
        Amount=Amount-withdrawl_amount
        print("The balance of your account is",Amount)

        transaction_history.append((datetime.datetime.now(),'Withdraw',withdrawl_amount))

def Credit_amount():
    global Amount
    print("You have selected the credit option")
    credit_amount=int(input("Enter the amount you want to credit in your bank"))
    Amount=Amount+credit_amount
    print("The balance of your account is",Amount)

    transaction_history.append((datetime.datetime.now(), 'Credit', credit_amount))
def transaction_hostory():
    if not transaction_history:
        print("No transactions yet")
    else:
        for transactions in transaction_history:
            print(transactions)

def run():
    global Amount
    if authenticate():
        while True:

            print("Menu:\n1. Withdrawal\n2. Credit Amount\n3. Check Balance\n4. View transactions\n5.Exit")
            n = (input("Enter your choice"))
            if n=='1':
                Withdrawl()
            elif n=='2':
                Credit_amount()
            elif n=='3':
                print("Balance is ",Amount)
            elif n=='4':
                transaction_hostory()
            elif n == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("invalid choice")
            time.sleep(2)

    else:
        print("Authentication failed")
run()