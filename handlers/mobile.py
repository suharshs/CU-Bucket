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
