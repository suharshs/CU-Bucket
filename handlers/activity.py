from base import BaseHandler
import simplejson as json
import re


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

        name = name.replace("\'", "\\'")
        name = name.replace("\"", "\\\"")
        description = description.replace("\'", "\\'")
        description = description.replace("\"", "\\\"")
        category = category.replace("\'", "\\'")
        category = category.replace("\"", "\\\"")
        location = location.replace("\'", "\\'")
        location = location.replace("\"", "\\\"")

        self.application.trie.add_token_words(name)

        sql = """INSERT INTO Activity (name, description, location, rating, creator)
            VALUES ('{0}', '{1}', '{2}', 0, '{3}')""".format(name, description, location, self.get_current_user())
        self.application.db.execute(sql)

        sql = " SELECT * FROM Activity WHERE ID = (SELECT MAX(ID) FROM Activity)"   # figure out the last id we input
        results = self.application.db.query(sql)
        id = results[0]['ID']
        print 'id', id

        category = re.sub(r"[^\w\s]", ' ', category)

        # whitespace-delimited category names
        for catname in category.split():
            sql = """INSERT INTO Category (name, activityID)
                VALUES (\'%s\', %s)""" % (catname, id)
            self.application.db.execute(sql)

        # first add relationship to userinterest table
        sql = " INSERT INTO UserInterest (userName, activityID) VALUES (\'%s\', %s)" % (self.get_current_user(), id)
        self.application.db.execute(sql)
        # next increment in Rating column of Activity table
        sql = " UPDATE Activity SET rating=rating+1 WHERE ID=%s " % (id)
        self.application.db.execute(sql)

        self.set_header("Content-Type", "application/json")
        was_successful = "true"
        info = {"passed": was_successful}
        info['userName'] = self.get_current_user()
        info['results'] = results
        self.write(json.dumps(info))
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


class CompleteActivityHandler(BaseHandler):
    def get(self, id):
        # first add relationship to usercompleted table
        sql = " INSERT INTO UserCompleted (userName, activityID) VALUES (\'%s\', %s)" % (self.get_current_user(), id)
        self.application.db.execute(sql)
        # next remove the activity from the users bucket
        sql = " DELETE FROM UserInterest WHERE userName = \'%s\' AND activityID = %s " % (self.get_current_user(), id)
        self.application.db.execute(sql)
        self.finish()


class DeleteActivityHandler(BaseHandler):
    def get(self, id):
        sql = "SELECT name FROM Activity WHERE ID = \'%s\'" % (id)
        self.application.trie.remove_token_words(self.application.db.query(sql)[0]["name"])
        sql = "DELETE FROM UserInterest WHERE activityID = \'%s\'" % (id)
        self.application.db.execute(sql)
        sql = "DELETE FROM UserCompleted WHERE activityID = \'%s\'" % (id)
        self.application.db.execute(sql)
        sql = "DELETE FROM Category WHERE activityID = \'%s\'" % (id)
        self.application.db.execute(sql)
        sql = "DELETE FROM Activity WHERE ID = \'%s\'" % (id)
        self.application.db.execute(sql)


class DeleteBucketActivityHandler(BaseHandler):
    def get(self, id):
        sql = " DELETE FROM UserInterest WHERE userName = \'%s\' AND activityID = %s " % (self.get_current_user(), id)
        self.application.db.execute(sql)
        # next increment in Rating column of Activity table
        sql = " UPDATE Activity SET rating=rating-1 WHERE ID=%s " % (id)
        self.application.db.execute(sql)
        self.finish()

