from base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, username):
        info = {'username': username}
        print '"' + username + '"'
        #self.render('user.html', info=info)


        username = self.get_current_user()
        info = {}


        # Get the activities created by the user
        sql = """
        SELECT * FROM Activity
        WHERE CREATOR = '{0}'
        ORDER BY Activity.ID DESC LIMIT 0, 20
        """.format(username)
        info['created'] = self.application.db.query(sql)


        # Get the user's bucket
        sql = """
        SELECT * FROM UserInterest ui
        JOIN Activity act 
        ON act.ID = ui.activityID
        WHERE ui.userName = '{0}'
        """.format(username)
        info['bucket'] = self.application.db.query(sql)


        info['recommendations'] = []  # this will have the pagerank results

        info['username'] = self.get_current_user()
        self.render('user.html', info=info)

        # Recommendations
        sql = """SELECT DISTINCT c.activityID AS 'ID', a.name, a.description, a.creator, a.rating, a.location
        FROM 
        (SELECT c.name, COUNT(c.activityID) AS 'activities'
         FROM UserInterest ui
        JOIN Activity a
        ON a.ID = ui.activityID
        JOIN Category c
        ON a.ID = c.activityID
        WHERE ui.userName = '{0}'
        GROUP BY c.name
        ORDER BY Count(c.activityID) DESC) bucket

        JOIN Category c
        ON c.name = bucket.name

        JOIN Activity a 
        ON a.ID = c.activityID

        LEFT JOIN UserInterest ui
        ON a.ID = ui.activityID

        WHERE ui.userName IS NULL 
        OR ui.userName != '{0}'""".format(username)
        info['recommendations'] = self.application.db.query(sql)


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
