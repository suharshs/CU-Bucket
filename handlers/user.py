from base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, username):
        info = {'username': username}
        print '"' + username + '"'
        #self.render('user.html', info=info)


        username = self.get_current_user()

        sql = """
        SELECT * FROM Activity
        WHERE CREATOR = '{0}'
        ORDER BY Activity.ID DESC LIMIT 0, 20
        """.format(username)

        print sql

        info = {}
        info['results'] = self.application.db.query(sql)

        if (self.get_current_user() == username or username == ''):
            info['username'] = self.get_current_user()
            self.render('user.html', info=info)
            # this is the user's personal page so we will show them all of the info
            pass
        else:
            # public user page, not everything is shown
            pass
