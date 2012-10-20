from base import BaseHandler
import simplejson as json


class SignupHandler(BaseHandler):
    def get(self):
        self.render('signup.html')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')

        created = self.create_user(username, password)
        if created:
            self.set_secure_cookie('username', username)  # set the session
            self.write(json.dumps({"passed": "true"}))
            self.finish()
        else:
            self.write(json.dumps({"passed": "false"}))
            self.finish()

    def create_user(self, username, password):
        sql = "SELECT name FROM User WHERE name = \"%s\" " % (username)
        results = self.application.db.query(sql)
        if (len(results) > 0):
            return False
        sql = "INSERT INTO User (name, password) VALUES (\"%s\", \"%s\")" % (username, password)
        self.application.db.execute(sql)
        return True
