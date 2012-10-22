from base import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        sql = """ SELECT * FROM Activity ORDER BY ID DESC LIMIT 0, 20""" 
        results = self.application.db.query(sql)
        self.render('home.html', results=results)
