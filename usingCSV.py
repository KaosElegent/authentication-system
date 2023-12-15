'''
Author: Shrey Bhatt
Date: December 11th, 2023
'''

from dbLogin import Dblogin


def login():
    details = Dblogin(input("Username: "), input("Password: "))

    if details.csvVerification("login.csv", "Username", "Password", "Salt"):
        print("Login Successful!\n")
    else:
        print("Invalid Credentials!\n")


def alter():
    while (True):
        details = Dblogin(input("Username: "), input("Password: "))
        if (input("Confirm? (y/n)").lower() == 'y'):
            break
        else:
            print("Enter again!\n")

    if details.setCsvCredentials(
            "login.csv", "Username", "Password", "Salt")[1]:
        print("Credentials Updated/Added Successfully!")
    else:
        print("There was a system error!")


def menu():
    while (True):
        print(
            """
    ----------------------------------------------------
    1) Login
    2) Add/Update Login Info
    0) Exit
    """)
        userInput = input("> ")

        match userInput:
            case '1':
                login()
            case '2':
                alter()
            case '0':
                break
            case _:
                print("Invalid Input!\n")


if __name__ == '__main__':
    menu()
