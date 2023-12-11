#os is used to generate a cryptographically strong salt. Alternative: secrets
import os

#haslib is used for generating hashes
import hashlib

class Dblogin:
    
    #The user's password is hashed and is never stored as plain text.
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.salt = None
    
    '''
    Description: This function is to be called once database connection has been made and there is a row with
                matching username.
    @param dbPassword: The salted password stored retrieved from the database.
    @param salt: The salt retrieved from the database.
    '''
    def verify(self, dbPassword, salt):
        #Hashing the password user entered with the salt from the database
        saltedPassword = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()[:32]

        if(dbPassword == saltedPassword): return True
        else: return False



if __name__ == '__main__':
    pass