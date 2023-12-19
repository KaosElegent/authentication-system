# Secure Login System

Hey there! This repo contains the **dbLogin** module. The DbLogin class can be used to manage and work with login credentials without worrying about hashing and salting yourself.

# Files

- **src/main.py** (Demo file to showcase the **DbLogin** class)
- **src/dblogin.py** (The DbLogin source file)
- **data/login.csv** (The CSV file used for the Demo)
- **data/sqlDatabase.sql** (The table structure used for querying)

# Why Salt and Hash?

This system can be used wherever password-based authentication is required.
### Normal password storage:

|Username|Password|
|-|-|
|User1|123456|
|User2|abcdefg123|
|User3|123user3|
|User4|123456|

### Hashed password storage (SHA-256):

|Username|Password|
|-|-|
|User1|8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92|
|User2|200f5183a8d9ef5339eaf6e3987d892e8751036beaa158257c1b65d78e3fa0f2|
|User3|a739cb1f52c35fd553252198fc98cee2135e1dc912f6dd640d0a667f4981fd80|
|User4|8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92|
 
#### Issues with this system
1) **User1** and **User4** have the same hash.
2) If the attacker has a hashlist of most common passwords, this makes the hashing process pointless.

> Note:
> While hashing the password is one-way and the original password isn't leaked, users with the same passwords (commonly used passwords) have the same hash, which makes it easy for the infiltrator to get everyone's credentials.

### Salted & Hashed password storage:

|Username|Password|Salt|
|-|-|-|
User1|411ac76c94b5587606b0314ddbfb2951cecc2278b85f14641f41f9092ac148e7|RCz7jheLX4mt+RZcRhf4IlOe+d9az0vMVQLnEMI1NV3lhO/v5Bdzd+FHf1fBfPHn
User2|db06d70ddd2d8b2fe981d9a56cb48ec2b9f227e9d79a05a56aeea8462e840bb0|2VvbCB7ix1RB2Es/kKKQzWLPqGIsTQZ+57C7yjdIpv5d+DjJEuApblgAJy3kNd+P
User3|c04acda7dbf4a5191fd2402c864313f9fbdeab6ef44913740692868902ceaaff|YHeYd9En6pV4N2kYEA6dh95ph7cSFoldTEHeaCiQn7Z8V5PxKtH8s8cMBxq6wDs9
User4|1ee2071b7009061186e640000f41f535af617f30b5e8305196df96c276cf1552|2C5eEgPe02O7/33x1at3hV5PyA2X+ogxP3A4egx44b79uzzTHYWcJnhX3yPAPrgB

Now, the users with the same original passwords have a uniquely hashed password since we added a salt during the hashing process. This 64 byte utf-8 decoded salt is randomly generated and is used to hash the original hashed password (100,000 times in the **DbLogin** system, before storage).

This renders hash lists completely useless and the attacker now has to spend a lot of time on every user's credentials.

# Implementation

- Create or Update an existing user :
New credentials (salt and a salted + hashed password) are created and stored.

- Authenticate an existing user :
Username and password (which gets hashed as soon as possible) are taken from the user. After which the,  password entered by the user is hashed using the salt from the database and cross referenced with the stored credentials.

# Working Demo

- The main menu :
![Main Menu](https://github.com/KaosElegent/database-login-system/blob/main/images/mainMenu.png?raw=true)
- User creation :
![User Creation](https://github.com/KaosElegent/database-login-system/blob/main/images/addUser.png?raw=true)
- User credentials updated :

- Invalid user credentials :

- Valid user credentials :


# Notes

- This project assumes that the password and salt are stored in seperate columns.
- The DbLogin functions will return return invalid authentication/credentials if more than 1 record has the same required username.
- The csv based functions assume that the file only contains 3 columns (username, password, salt)
