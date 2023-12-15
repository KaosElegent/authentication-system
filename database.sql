CREATE TABLE loginInfo(
    loginid int AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    salt CHAR(64)
    PRIMARY KEY(loginid)
);