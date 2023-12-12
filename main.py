'''
Author: Shrey Bhatt
Date: December 11th, 2023
'''
# Requirements
#import pymysql.cursors    #If using pymysql for database connection
import csv                 #If using csv files
import base64              #For storing the bytes of salt in a csv
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
            if details.username == row[0]:
                
                if details.verify(row[1],row[2]):
                    print ("Login Successful!\n")
                else:
                    print ("Information Entered Was Incorrect!\n")
                return
        print ("Information Entered Was Incorrect!\n")
        return

def alter():
    while(True):
        details = Dblogin(input("Username: "), input("Password: "))
        if(input("Confirm? (y/n)").lower() == 'y'): break
        else: print("Enter again!\n")

    saltedPassword, salt = details.setCredentials()
    with open('login.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([details.username, saltedPassword, salt]) 

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


