import math
print("Welcome to BASE: An Online Banking Application")


def signup():
    global name
    global pin
    global currentBalance
    name = str(input("Enter an username"))
    pin = str(input("Enter your 6 digit PIN"))
