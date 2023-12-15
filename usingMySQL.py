'''
Author: Shrey Bhatt
Date: December 14th, 2023
'''

# To use environment variables
import os

# Since I'm using a MySQL database for demo here
import pymysql.cursors

# To get ca certificates for databse connection
import certifi

from dbLogin import Dblogin

# The database connection object
connection = pymysql.connect(host=os.getenv("DEMO_HOST"),
                             user=os.getenv("DEMO_USERNAME"),
                             password=os.getenv("DEMO_PASSWORD"),
                             database=os.getenv("DEMO_DATABASE"),
                             cursorclass=pymysql.cursors.DictCursor,

                             autocommit=False,
                             ssl_verify_identity=True,
                             ssl={
                             "ca": certifi.where()
                             })
cursor = connection.cursor()
