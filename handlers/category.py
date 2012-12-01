from base import BaseHandler

class CategoryHandler(BaseHandler):
    def get(self, category):
        info = {}
        info['username'] = self.get_current_user()

        sql = """
        SELECT DISTINCT name FROM Category c ORDER BY name
        """
        info['categories'] = self.application.db.query(sql)

        if category == '':
            info['activities'] = []
        else:   # A specific category
            sql = """
            SELECT * FROM Activity a
            WHERE a.ID IN 
            (SELECT activityID FROM Category 
            WHERE name = '{0}')
            """.format(category)
            info['activities'] = self.application.db.query(sql)


        self.render('category.html', info=info)

