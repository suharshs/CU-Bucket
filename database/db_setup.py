from tornado.database import Connection
from urlparse import urlparse
import sys
# This file is a script that setups the database for cucket if the tables don't already exist

#DATABASE_URL = sys.argv[1]
#url = urlparse(DATABASE_URL)

#db = Connection(host=url.hostname, user=url.username, password=url.password, database=url.path[1:])
#db = Connection(host="engr-cpanel-mysql.engr.illinois.edu", user="cubucket_root", password="cucket", database="cubucket_db")
db = Connection(host='localhost:3306', user='root', password='', database='cucket')  # will later need to change this for heroku


# Drop the existing tables
tables = ['UserCompleted', 'UserInterest', 'Category', 'Activity', 'User']
for table in tables:
    sql = "DROP TABLE IF EXISTS `{0}`".format(table)
    db.execute(sql)


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
    creator varchar(15) NOT NULL,\
    rating int NOT NULL,\
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
