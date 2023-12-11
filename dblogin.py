# os is used to generate a cryptographically strong salt. Alternative: secrets
import os

# haslib is used for generating hashes
import hashlib

class Dblogin:
    
    # The user's password is hashed and is never stored as plain text.
    def __init__(self, username, password):
        if()
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.salt = None
    
    '''
    Description: This function is to be called once database connection
                has been made and there is a record with matching username.
    @param dbPassword: The salted password stored retrieved from the database.
    @param salt: The salt retrieved from the database.
    @returns boolean: True if the credentials match, else False.
    '''
    def verify(self, dbPassword, salt):
        # Hashing the password user entered with the salt from the database
        saltedPassword = hashlib.pbkdf2_hmac('sha256',
                                             self.password.encode('utf-8'),
                                             salt.encode('utf-8'),
                                             100000).hex()[:32]

        if(dbPassword == saltedPassword): return True
        else: return False

    '''
    Description: This function uses string formatting & parameterized
                queries to safely query a database via the cursor.
    '''
    def sqlVerification(self, cursor,
                        tableName, usernameCol, passwordCol, saltCol):

        # Parameterized Query
        query = "SELECT * FROM %s WHERE %s = '%s'"
        cursor.execute(query, (tableName, usernameCol, self.username))

        # If such a column was found in the database
        if(cursor.fetchall() != ()):

            # Fetch the first row (Ideally there's only 1 row)
            record = cursor.fetchall()[0] 
            if self.verify(record[passwordCol], record[saltCol]):
                return True

        return False

    
    



if __name__ == '__main__':
    pass