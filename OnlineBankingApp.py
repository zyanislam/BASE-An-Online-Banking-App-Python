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
    if len(recoverPin) != 6:
        print("<< Error: Invalid PIN >>")
        print("The PIN must have 6 digits.\n")
        forgotPin()
    else:
        print("Congratulations! The new PIN has been stored")
        print("Please Sign-In Now!")
        pin = recoverPin


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

    else:
        print("<< Error: Your User or Password does not match or it does not exist. >>")
        print("Have you created your BASE Account.\n")
        list1 = ["1: Yes\n", "2: Non\n"]
        for i in list1:
            print(i)

        inp = int(input("Enter your choice: "))
        if inp == 1:
            list2 = ["1: Retry to Login into your BASE Account\n",
                     "2: Forgot your password?\n"]
            for j in list2:
                print(j)

            choice = int(input("Enter your choice: "))
            if choice == 1:
                login()
            elif choice == 2:
                forgotPin()
            else:
                print("<< ERROR: Your Choice " + choice + "is not valid. >>")
