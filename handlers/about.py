from base import BaseHandler
import simplejson as json


class AboutHandler(BaseHandler):

    def get(self):
        info = {}
        info['username'] = self.get_current_user()
        self.render('about.html', info=info)
