from tornado.database import Connection
from urlparse import urlparse
import sys
# This file is a script that setups the database for cucket if the tables don't already exist
DATABASE_URL = sys.argv[1]
url = urlparse(DATABASE_URL)

db = Connection(host=url.hostname, user=url.username, password=url.password, database=url.path[1:])


# Drop the existing tables
sql = """\
DROP TABLE IF EXISTS `usercompleted`;\
DROP TABLE IF EXISTS `userinterest`;\
DROP TABLE IF EXISTS `category`;\
DROP TABLE IF EXISTS `activity`;\
DROP TABLE IF EXISTS `user`;\
"""
try:
    db.execute(sql)
except:
    print "error deleting tables"


# Create the User table
sql = """CREATE TABLE IF NOT EXISTS User(\
    name varchar(15) NOT NULL PRIMARY KEY,\
    password varchar(100) NOT NULL\
);"""
db.execute(sql)

# Create the Activity table
sql = """CREATE TABLE IF NOT EXISTS Activity(\
    ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,\
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
