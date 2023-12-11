'''
Author: Shrey Bhatt
Date: December 11th, 2023
'''
# Requirements
import pymysql.cursors #If using pymysql for database connection


# Sample SQL Connecton (For this Demo, I'll be using CSV to simulate a database)
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


# Functions


