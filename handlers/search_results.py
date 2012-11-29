from base import BaseHandler
from lev_dist.levenshtein_distance import *


class SearchResultsHandler(BaseHandler):
    def get(self, word):
    	
        sql = """ SELECT * FROM Activity LEFT JOIN (SELECT * FROM UserInterest WHERE userName='%s') as currUserInterest ON Activity.ID = currUserInterest.activityID WHERE  DESC LIMIT 0, 20""" % (self.get_current_user())
        info = {}
        info['results'] = self.application.db.query(sql)
        info['username'] = self.get_current_user()
        self.render('top.html', info=info)