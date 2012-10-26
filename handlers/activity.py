from base import BaseHandler
import simplejson as json


class ActivityHandler(BaseHandler):

    def post(self):
        print "ActivityHandler"
        name = self.get_argument('name', '')
        description = self.get_argument('description', '')
        category = self.get_argument('category', '')
        location = self.get_argument('location', '')

        print 'name ', name
        print 'description ', description
        print 'category ', category
        print 'location ', location

        sql = " INSERT INTO Activity (name, description, location, rating, creator) VALUES (\'%s\', \'%s\', \'%s\', 0, \'%s\') " % (name, description, location, self.get_current_user())
        self.application.db.execute(sql)

        sql = " SELECT MAX(ID) FROM Activity "   # figure out the last id we input
        id = self.application.db.query(sql)[0]['MAX(ID)']
        print 'id', id

        sql = " INSERT INTO Category (name, activityID) VALUES (\'%s\', %s) " % (category, id)
        self.application.db.execute(sql)

        self.set_header("Content-Type", "application/json")
        was_successful = "true"
        self.write(json.dumps({"passed": was_successful}))
        self.finish()


class RatingHandler(BaseHandler):
    def get(self, id):
        # first add relationship to userinterest table
        sql = " INSERT INTO UserInterest (userName, activityID) VALUES (\'%s\', %s)" % (self.get_current_user(), id)
        self.application.db.execute(sql)
        # next increment in Rating column of Activity table
        sql = " UPDATE Activity SET rating=rating+1 WHERE ID=%s " % (id)
        self.application.db.execute(sql)
        self.finish()


class DeleteActivityHandler(BaseHandler):
    def get(self, id):
        sql = "DELETE FROM UserInterest WHERE activityID = \'%s\'" % (id)
        self.application.db.execute(sql)
        sql = "DELETE FROM UserCompleted WHERE activityID = \'%s\'" % (id)
        self.application.db.execute(sql)
        sql = "DELETE FROM Category WHERE activityID = \'%s\'" % (id)
        self.application.db.execute(sql)
        sql = "DELETE FROM Activity WHERE ID = \'%s\'" % (id)
        self.application.db.execute(sql)
