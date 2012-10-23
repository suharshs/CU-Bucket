from base import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        sql = """ SELECT * FROM Activity ORDER BY ID DESC LIMIT 0, 20"""
        info = {}
        info['results'] = self.application.db.query(sql)
        info['username'] = self.get_current_user()
        self.render('home.html', info=info)
