"""
Mobile app handlers
"""

from base import MobileHandler
import simplejson as json


class MobileLoginHandler(MobileHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')

        auth = self.authenticate(username, password)

        if auth:
            self.write(json.dumps({"passed": "true"}))
            self.finish()
        else:
            self.write(json.dumps({"passed": "false"}))
            self.finish()

    def authenticate(self, username, password):
        # returns true if the username matches the password in the database
        sql = """ SELECT name FROM User WHERE name = \"%s\" AND password = \"%s\" """ % (username, password)
        results = self.application.db.query(sql)
        if (len(results) < 1):
            return False
        return True


class MobileUserBucketHandler(MobileHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")
        username = self.get_argument('username', '')

        sql = "SELECT * FROM UserInterest ui JOIN Activity act ON act.ID = ui.activityID WHERE ui.userName = \'%s\'" % (username)
        results = self.application.db.query(sql)
        self.write({"bucket": results})
        self.finish()


class MobileCompleteActivityHandler(MobileHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")
        username = self.get_argument('username', '')
        id = self.get_argument('id', '')

        sql = " INSERT INTO UserCompleted (userName, activityID) VALUES (\'%s\', %s)" % (username, id)
        self.application.db.execute(sql)
        # next remove the activity from the users bucket
        sql = " DELETE FROM UserInterest WHERE userName = \'%s\' AND activityID = %s " % (username, id)
        self.application.db.execute(sql)

        self.write({"success": "true"})
        self.finish()


class MobileAddActivityHandler(MobileHandler):
    def post(self):
        name = self.get_argument('name', '')
        description = self.get_argument('description', '')
        category = self.get_argument('category', '')
        location = self.get_argument('location', '')
        username = self.get_argument('username', '')

        sql = """INSERT INTO Activity (name, description, location, rating, creator)
            VALUES ('{0}', '{1}', '{2}', 0, '{3}')""".format(name, description, location, username)
        self.application.db.execute(sql)

        sql = " SELECT * FROM Activity WHERE ID = (SELECT MAX(ID) FROM Activity)"   # figure out the last id we input
        results = self.application.db.query(sql)
        id = results[0]['ID']
        print 'id', id

        # whitespace-delimited category names
        for catname in category.split():
            sql = """INSERT INTO Category (name, activityID)
                VALUES (\'%s\', %s)""" % (catname, id)
            self.application.db.execute(sql)

        # first add relationship to userinterest table
        sql = " INSERT INTO UserInterest (userName, activityID) VALUES (\'%s\', %s)" % (username, id)
        self.application.db.execute(sql)
        # next increment in Rating column of Activity table
        sql = " UPDATE Activity SET rating=rating+1 WHERE ID=%s " % (id)
        self.application.db.execute(sql)

        self.set_header("Content-Type", "application/json")
        was_successful = "true"
        info = {"passed": was_successful}
        info['id'] = id
        self.write(json.dumps(info))
        self.finish()
