'''
Author: Shrey Bhatt
Date: December 11th, 2023
'''
# Requirements
#import pymysql.cursors    #If using pymysql for database connection
import csv                 #If using csv files
from saltedLogin import Dblogin


# Database Connection (For this Demo, I'll be using CSV to simulate a database
#                      But the following syntax can be used to work
#                      with Dblogin objects.
'''
connection = pymysql.connect(host=os.getenv("HOST"),
                             user=os.getenv("USERNAME"),
                             password=os.getenv("PASSWORD"),
                             database=os.getenv("DATABASE"),
                             cursorclass=pymysql.cursors.DictCursor,

                             autocommit = True,
                             ssl_verify_identity = True,
                             ssl      = {
                             "ca": <CA Certificate Location>
                             })
cursor = connection.cursor()
'''

def login():
    # Try: Elegent, test123
    details = Dblogin(input("Username: "), input("Password: "))

    with open('login.csv', newline='\n') as csvFile:

        rows = csv.reader(csvFile, delimiter=',')
        for row in rows:
            if details.username == row[1]:
                print(row[3])
                if details.verify(row[2],bytes(row[3], 'utf-8')):
                    print ("Login Successful!\n")
                else:
                    print ("Information Entered Was Incorrect!\n")
                return
        print ("Information Entered Was Incorrect!\n")
        return



def menu():
    while(True):
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


