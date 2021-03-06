from base import BaseHandler
import simplejson as json


class LoginHandler(BaseHandler):
    def get(self):
        if not self.get_current_user():
            self.render('login.html')
            return
        #self.redirect('/user/%s' % (self.get_current_user()))
        self.redirect('/home')

    def post(self):
        self.set_header("Content-Type", "application/json")
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')

        auth = self.authenticate(username, password)

        if auth:
            self.set_secure_cookie('username', username)  # set the session
            self.write(json.dumps({"passed": "true"}))
            self.finish()
        else:
            self.write(json.dumps({"passed": "false"}))
            self.finish()

    def authenticate(self, username, password):
        # returns true if the username matches the password in the database
        sql = """ SELECT name FROM User WHERE name = \"%s\" AND password = \"%s\" """ % (username, password)
        results = self.application.db.query(sql)
        if (len(results) < 1):
            return False
        return True


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('username')
        self.redirect('/login')
