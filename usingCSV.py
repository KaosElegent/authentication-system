'''
Author: Shrey Bhatt
Date: December 11th, 2023
'''

# Since I'm using csv for demo here
import pandas as pd

import csv

from dbLogin import Dblogin

def login():
    details = Dblogin(input("Username: "), input("Password: "))

    df = pd.read_csv('login.csv')

    row =  df.loc[df['Username'] == details.username]

    print(row)

    '''
    if(len(row) == 1):
        if details.verify(row[1], row[2].encode('utf-8')):
                    print ("Login Successful!\n")
                else:
                    print ("Information Entered Was Incorrect!\n")
    '''
                    
    '''
    with open('login.csv', newline='\n') as csvFile:

        rows = csv.reader(csvFile, delimiter=',')
        for row in rows:
            if details.username == row[0]:
                
                if details.verify(row[1], row[2].encode('utf-8')):
                    print ("Login Successful!\n")
                else:
                    print ("Information Entered Was Incorrect!\n")
                return
        print ("Information Entered Was Incorrect!\n")
        return
    '''

def alter():
    while(True):
        details = Dblogin(input("Username: "), input("Password: "))
        if(input("Confirm? (y/n)").lower() == 'y'): break
        else: print("Enter again!\n")

    saltedPassword, salt = details.setCredentials(strSalt=True)
    with open('login.csv', 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([details.username, saltedPassword, salt.decode('utf-8')])

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


