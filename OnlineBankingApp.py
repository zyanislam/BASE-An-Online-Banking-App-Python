from asyncio import wait
import math
print("Welcome to BASE: An Online Banking Application")


def signUp():
    global user
    global pin
    global currentBalance

    user = str(input("Enter your username: "))
    pin = str(input("Enter your 6 digit PIN: "))

    if len(pin) == 6:
        pin = pin
    else:
        print("<< Error: Invalid PIN >>")
        print("The PIN must have 6 digits.\n")
        newPin = str(input("Enter your 6 digit PIN: "))
        if len(newPin) != 6:
            print("<< Error: Invalid PIN >>")
            print("The PIN must have 6 digits.\n")
            signUp()
        else:
            pin = newPin
    print("Congratulations! You have successfully signed up")


def forgotPin():
    recoverPin = str(input("Enter your new 6 digits Pin: "))
    if len(recoverPin) == 6:
        pin = recoverPin
        print("Congratulations! The new PIN has been stored")
        print("Please Sign-In Now!")
        login()
    else:
        print("<< Error: Invalid PIN >>")
        print("The PIN must have 6 digits.\n")
        forgotPin()


def balanceInterest(current, rate, time):
    # Compound Interest Formula
    # A = Pe^(rt)
    current = float(current)
    rate = float(rate)
    time = float(time)
    rt = rate * time
    expo = math.exp(rt)
    a = current * expo
    return a


def login():
    user1 = str(input("Enter your username: "))
    pin1 = str(input("Enter your password: "))

    if user1 == user and pin1 == pin:
        print("Welcome to BASE: An Online Banking Application" + " " + user + "\n")
        print("Choose your option from the menu below")
        menu = ["1: Check Your Account Balance", "2: Withdraw Money", "3: Transfer Money",
                "4: Deposit Money", "5: Deposite Interest Rate", "6: Calculate Compound Interest"]
        for a in menu:
            print(a)
        choice = int(input("Enter your choice: "))
        deposite = 0
        withdraw = 0
        currentBalance = 0

        if choice == 1:
            print("Current Account Balance: " + currentBalance)
        elif choice == 2:
            print("Current Account Balance: " + currentBalance)
        elif choice == 3:
            print("Current Account Balance: " + currentBalance)
        elif choice == 4:
            print("Current Account Balance: " + currentBalance)
            deposite = int(input("Enter the ammount you want to deposit: "))
            currentBalance = currentBalance + deposite
            int("Current Account Balance: " + currentBalance)

    else:
        print("<< Error: Your User or Password does not match or it does not exist. >>")
        print("Have you created your BASE Account?\n")
        list1 = ["1: Yes", "2: No"]
        for b in list1:
            print(b)

        inp = int(input("Enter your choice: "))
        if inp == 1:
            list2 = ["1: Retry to Login into your BASE Account",
                     "2: Forgot your password?"]
            for c in list2:
                print(c)

            choice = int(input("Enter your choice: "))
            if choice == 1:
                login()
            elif choice == 2:
                forgotPin()
            else:
                print("<< ERROR: Your Choice " + choice + "is not valid. >>")
                login()

        elif inp == 2:
            print("Please create your BASE Account first.")
            print(">> Redirecting to BASE SignUp.")
            wait(500)
            signUp()
