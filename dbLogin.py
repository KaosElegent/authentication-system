# haslib is used for generating hashes
import hashlib

# os is used to generate a cryptographically strong salt. Alternative: secrets
from os import urandom

# b64encode is used to convert the random 32 byte salt to a
# 32 byte utf-8 string for storage in string format
from base64 import b64encode


class Dblogin:

    # The user's password is hashed and is never stored as plain text.
    # Note: This object uses the salt as a byte-like object.
    # But for real use case a normal 32 byte string would be used
    def __init__(self, username, password):
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
                                             salt,
                                             100000).hex()[:32]

        if (dbPassword == saltedPassword):
            return True
        else:
            return False

    '''
    Description: This function uses string formatting & parameterized
                queries to safely query a database via the cursor.
    @param cursor: A pymysql (or similar) connection cursor object
                used for connecting to the SQL database.
    @param tableName: A string representing the table name where
                login data is stored.
    @param usernameCol: A string representing the column name where
                the username is stored.
    @param passwordCol: A string representing the column name where
                the salted password is stored.
    @param saltCol: A string representing the column name where
                the salt is stored.
    @returns boolean: True if the credentials match, else False.
    '''

    def sqlVerification(self, cursor,
                        tableName, usernameCol, passwordCol, saltCol):

        # Parameterized Query (safeguard against SQL Injection)
        query = "SELECT * FROM %s WHERE %s = '%s'"
        cursor.execute(query, (tableName, usernameCol, self.username))

        # If such a column was found in the database
        if (cursor.fetchall() != ()):

            # Fetch the first row (Ideally there's only 1 row)
            record = cursor.fetchall()[0]
            if self.verify(record[passwordCol], record[saltCol]):
                return True

        return False

    '''
    Description: This function is used for updating the current salt
                and returning the new salted password.
    @param strSalt: This is a flag (False by default).
                If True, the salt generated has bytes that
                can be decoded to utf-8.
                If False, the random salt generated has random
                bytes which can't be decoded to utf-8.
    @returns 2 values: salted password, salt
    '''

    def setCredentials(self, strSalt=0):

        # 32 Random cryptografically safe bytes
        '''
        The 32 randombytes from urandom are encoded in base64
        to remove any non utf-8 bytes. Having utf-8 bytes might
        sound less secure but this makes it easier to store and
        work with the byte-like object while keeping it just as
        randomized.
        '''
        if strSalt:
            self.salt = b64encode(urandom(32))[:32]
        else:
            self.salt = urandom(32)

        saltedPassword = hashlib.pbkdf2_hmac('sha256',
                                             self.password.encode('utf-8'),
                                             self.salt,
                                             100000).hex()[:32]
        return saltedPassword, self.salt

    '''
    Description: This function is used for updating the current salt
                and returning the new salted password.
    @param cursor: A pymysql (or similar) connection cursor object
                used for connecting to the SQL database.
    @param tableName: A string representing the table name where
                login data is stored.
    @param usernameCol: A string representing the column name where
                the username is stored.
    @param passwordCol: A string representing the column name where
                the salted password is stored.
    @param saltCol: A string representing the column name where
                the salt is stored.
    @returns 2 values: salted password, salt
    '''

    def setSqlCredentials(self, cursor,
                          tableName, usernameCol, passwordCol, saltCol):

        saltedPassword = self.newCredentials()[0]

        # Parameterized Query (safeguard against SQL Injection)
        query = "SELECT * FROM %s WHERE %s = '%s'"
        cursor.execute(query, (tableName, usernameCol, self.username))

        # If such a column was found in the database
        if (cursor.fetchall() != ()):
            query = "UPDATE %s SET %s = %s, %s = %s WHERE %s = '%s'"
            cursor.execute(query, (tableName,
                                   passwordCol, saltedPassword, saltCol,
                                   str(self.salt), usernameCol, self.username))
        else:
            query = "INSERT INTO %s(%s, %s, %s) VALUES(%s, %s, %s)"
            cursor.execute(query, (tableName,
                                   usernameCol, passwordCol, saltCol,
                                   self.username, saltedPassword, str(self.salt)))

        return saltedPassword, self.salt


if __name__ == '__main__':
    test = Dblogin("Kaos", "test123")
    print(test.setCredentials())
