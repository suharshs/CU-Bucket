from base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        sql = """ SELECT * FROM Activity LEFT JOIN (SELECT * FROM UserInterest WHERE userName=\'%s\') as currUserInterest ON Activity.creator = currUserInterest.userName ORDER BY Activity.ID DESC LIMIT 0, 20""" % (self.get_current_user())
        info = {}
        info['results'] = self.application.db.query(sql)
        info['username'] = self.get_current_user()
        self.render('home.html', info=info)
