from base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, username):
        info = {'username': username}
        print '"' + username + '"'
        #self.render('user.html', info=info)


        username = self.get_current_user()
        info = {}

        # Get the activities created by the user
        sql = """ SELECT * FROM Activity a
        LEFT JOIN (SELECT userName as interestUserName, activityID 
            FROM UserInterest WHERE userName='{0}') 
        AS currUserInterest 
        ON a.ID = currUserInterest.activityID 
        LEFT JOIN (SELECT userName as completedUserName, activityID 
            FROM UserCompleted WHERE userName='{0}') 
        AS currUserComplete 
        ON a.ID = currUserComplete.activityID 
        WHERE a.creator='{0}'
        ORDER BY a.ID DESC 
        LIMIT 0, 20""".format(username)
        info['created'] = self.application.db.query(sql)


        # Get the user's bucket
        sql = """
        SELECT * FROM UserInterest ui
        JOIN Activity act 
        ON act.ID = ui.activityID
        WHERE ui.userName = '{0}'
        """.format(username)
        info['bucket'] = self.application.db.query(sql)


        # Completed activities 
        sql = """
        SELECT * FROM UserCompleted uc
        JOIN Activity act 
        ON act.ID = uc.activityID
        WHERE uc.userName = '{0}'
        """.format(username)
        info['completed'] = self.application.db.query(sql)



        # Progress bar percentages
        info['bucket_count'] = min(len(info['bucket']), 100)
        info['completed_count'] = min(len(info['completed']), 100)
        



        # Recommendations
        # Based on number of matching categories.  Any activities not in the user's
        # bucket are eligible.  Categories are compared to both completed
        # and incomplete bucketed activities
        sql = """SELECT DISTINCT c.activityID AS 'ID', a.name, a.description, a.creator, a.rating, a.location
        FROM 
        (
           SELECT c.name, COUNT(c.activityID) AS 'activities'
           FROM Category c
           JOIN Activity a
               ON a.ID = c.activityID
           WHERE a.ID IN 
               (SELECT ID FROM UserInterest ui
               JOIN Activity a ON a.ID = ui.activityID
               WHERE ui.userName = '{0}') 
           OR a.ID IN 
               (SELECT ID FROM UserCompleted uc
               JOIN Activity a ON a.ID = uc.activityID
               WHERE uc.userName = '{0}')
           GROUP BY c.name
           ORDER BY activities DESC 
        ) bucket
        JOIN Category c
            ON c.name = bucket.name
        JOIN Activity a 
            ON a.ID = c.activityID
        LEFT JOIN UserInterest ui
            ON a.ID = ui.activityID
        LEFT JOIN UserCompleted uc
            ON a.ID = uc.activityID
        WHERE (ui.userName IS NULL 
            OR ui.userName != '{0}')
        AND 
        (uc.userName IS NULL 
            OR uc.userName != '{0}')
        LIMIT 0, 20
        """.format(username)
        info['recommendations'] = self.application.db.query(sql)
        print info['recommendations']


        info['username'] = self.get_current_user()
        self.render('user.html', info=info)


        """
        if (self.get_current_user() == username or username == ''):
            info['username'] = self.get_current_user()
            self.render('user.html', info=info)
            # this is the user's personal page so we will show them all of the info
            pass
        else:
            # public user page, not everything is shown
            pass
        """
