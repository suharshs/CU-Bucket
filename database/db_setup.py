from tornado.database import Connection

# This file is a script that setups the database for cucket if the tables don't already exist

db = Connection(host='localhost:3306', user='root', password='', database='cucket')

# Create the User table
sql = """CREATE TABLE IF NOT EXISTS User(\
    name varchar(15) NOT NULL PRIMARY KEY,\
    password varchar(100) NOT NULL\
);"""
db.execute(sql)

# Create the Activity table
sql = """CREATE TABLE IF NOT EXISTS Activity(\
    ID int NOT NULL PRIMARY KEY,\
    name varchar(100) NOT NULL,\
    description varchar(500),\
    ranking int NOT NULL,\
    location varchar(100)\
);"""
db.execute(sql)

# Create the Category table
sql = """CREATE TABLE IF NOT EXISTS Category(\
    name varchar(100) NOT NULL PRIMARY KEY,\
    activityID int NOT NULL,\
    FOREIGN KEY (activityID) REFERENCES Activity(ID)\
);"""
db.execute(sql)

# Create the UserInterest tables
sql = """CREATE TABLE IF NOT EXISTS UserInterest(\
    userName varchar(15) NOT NULL,\
    activityID int NOT NULL,\
    FOREIGN KEY (userName) REFERENCES User(name),\
    FOREIGN KEY (activityID) REFERENCES Activity(ID)\
);"""
db.execute(sql)

# Create the UserCompleted table
sql = """CREATE TABLE IF NOT EXISTS UserCompleted(\
    userName varchar(15) NOT NULL,\
    activityID int NOT NULL,\
    FOREIGN KEY (userName) REFERENCES User(name),\
    FOREIGN KEY (activityID) REFERENCES Activity(ID)\
);"""
db.execute(sql)

db.close()
