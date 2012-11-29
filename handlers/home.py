from base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        sql = """ SELECT * FROM Activity LEFT JOIN (SELECT userName as interestUserName, activityID FROM UserInterest WHERE userName='%s') as currUserInterest ON Activity.ID = currUserInterest.activityID LEFT JOIN (SELECT userName as completedUserName, activityID FROM UserCompleted WHERE userName='%s') as currUserComplete ON Activity.ID = currUserComplete.activityID ORDER BY Activity.ID DESC LIMIT 0, 20""" % (self.get_current_user(), self.get_current_user)
        info = {}
        info['results'] = self.application.db.query(sql)
        info['username'] = self.get_current_user()
        self.render('home.html', info=info)
