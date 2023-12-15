'''
Author: Shrey Bhatt
Date: December 14th, 2023
'''

# To use environment variables
import os
import load_dotenv
load_dotenv()

# Since I'm using a MySQL database for demo here
import pymysql.cursors

# To get ca certificates for databse connection
import certifi

from dbLogin import Dblogin

# The database connection object
connection = pymysql.connect(host=os.getenv("DATABASE_HOST"),
                             user=os.getenv("DATABASE_USERNAME"),
                             password=os.getenv("DATABASE_PASSWORD"),
                             database=os.getenv("DATABASE"),
                             cursorclass=pymysql.cursors.DictCursor,

                             autocommit=False,
                             ssl_verify_identity=True,
                             ssl={
                             "ca": certifi.where()
                             })
cursor = connection.cursor()


def login():
    details = Dblogin(input("Username: "), input("Password: "))

    if details.sqlVerification(cursor, "loginInfo",
                               "username", "password", "salt"):
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

    if details.setSqlCredentials(cursor, "loginInfo",
                                 "username", "password", "salt")[1]:
        print("Credentials Altered Successfully!")
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
