from base import BaseHandler
import simplejson as json


class SignupHandler(BaseHandler):
    def get(self):
        self.render('signup.html')

    def post(self):
        self.get_argument('username', '');
        self.get_argument('password', '');