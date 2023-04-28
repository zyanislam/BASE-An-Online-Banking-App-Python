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
                "4: Deposit Money", "5: Check Deposite Interest Rate", "6: Calculate Compound Interest"]
        for a in menu:
            print(a)
        choice = int(input("Enter your choice: "))
        deposite = 0
        withdraw = 0
        currentBalance = 0

        if choice == 1:
            print("Current Account Balance: " + str(currentBalance))

        elif choice == 2:
            print("Current Account Balance: " + str(currentBalance))
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw > currentBalance:
                print("Your current account balace is not sufficient for a transaction.")
            else:
                currentBalance = currentBalance - withdraw
                print(str(withdraw) +
                      " has been withdrawn from your current account.")
                print("Current Account Balance: " + str(currentBalance))

        elif choice == 3:
            print("Current Account Balance: " + str(currentBalance))
            destination = str(input("Enter the 8 digit account no: "))
            if len(destination) == 8:
                amount = int(input("Enter the amount you want to transfer: "))
                if amount > currentBalance:
                    print(
                        "Your current account balace is not sufficient for a transaction.")
                    login()
                else:
                    currentBalance = currentBalance - amount
                    print(str(withdraw) +
                          " has been transfered from your current account to amount " + destination)
                    print("Current Account Balance: " + str(currentBalance))
            else:
                print("<< Error: Your Account No is invalid.")
                login()

        elif choice == 4:
            print("Current Account Balance: " + str(currentBalance))
            deposite = int(input("Enter the amount you want to deposit: "))
            currentBalance = currentBalance + deposite
            print("Current Account Balance: " + str(currentBalance))

        elif choice == 5:
            if deposite > 50000:
                rate = 3
            elif deposite > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Your Current Deposite Interest Rate: " + str(rate) + " %")

        elif choice == 6:
            option = ["1: Calculate Deposite Compount Interest based on your Current Balance",
                      "2: Calculate Deposite Compount Interest based on your Deposite Input"]
            for n in option:
                print(n)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                timing = str(
                    input("Enter the no of years you want to invest your money for: "))
                if deposite > 50000:
                    ratex = 3/100
                elif deposite > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print("Current Account Balance in " + timing +
                      " years will be")
                print(balanceInterest(currentBalance, ratex, timing))
            elif choice == 2:
                timing = str(
                    input("Enter the no of years you want to invest your money for: "))
                money = str(input("Enter the amount you want to deposit: "))
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
                print("<< ERROR: Your Choice " +
                      str(choice) + "is not valid. >>")
                login()

        elif inp == 2:
            print("Please create your BASE Account first.")
            print(">> Redirecting to BASE SignUp.")
            signUp()
