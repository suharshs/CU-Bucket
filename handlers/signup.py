from base import BaseHandler
import simplejson as json


class SignupHandler(BaseHandler):
    def get(self):
        self.render