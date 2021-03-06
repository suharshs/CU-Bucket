from base import BaseHandler


class TopHandler(BaseHandler):
    def get(self):
        sql = """ SELECT * FROM Activity 
        LEFT JOIN (SELECT userName as interestUserName, activityID 
            FROM UserInterest WHERE userName='{0}') 
        AS currUserInterest ON 
        Activity.ID = currUserInterest.activityID 
        LEFT JOIN (SELECT userName as completedUserName, activityID 
            FROM UserCompleted WHERE userName='{0}') 
        AS currUserComplete 
        ON Activity.ID = currUserComplete.activityID 
        ORDER BY Activity.rating DESC LIMIT 0, 20""".format(self.get_current_user())
        info = {}
        info['results'] = self.application.db.query(sql)
        info['username'] = self.get_current_user()
        self.render('top.html', info=info)