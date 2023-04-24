import math
print("Welcome to BASE: An Online Banking Application")


def signUp():
    global name
    global pin
    global currentBalance

    name = str(input("Enter an username: "))
    pin = str(input("Enter your 6 digit PIN: "))

    if len(pin) == 6:
        pin = pin
    else:
        print("Error: Invalid PIN")
        print("The PIN must have 6 digits.")
        newPin = str(input("Enter your 6 digit PIN: "))
        if len(newPin) != 6:
            print("Error: Invalid PIN")
            print("The PIN must have 6 digits.")
            signUp()
        else:
            pin = newPin
    print("Congratulations! You have successfully signed up")


def forgotPin():
    recoverPin = str(input("Enter your new 6 digits Pin: "))
    if len(recoverPin) != 6:
        print("Error: Invalid PIN")
        print("The PIN must have 6 digits.")
        forgotPin()
    else:
        print("Congratulations! The new PIN has been stored")
        print("Please Sign-In Now!")
        pin = recoverPin
