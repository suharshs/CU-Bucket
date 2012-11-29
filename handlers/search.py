from base import BaseHandler
from lev_dist.levenshtein_distance import *
import simplejson as json


class SearchHandler(BaseHandler):
    """
        This handler gives the closest activities to the ones that the user typed in the search bar
    """
    def get(self):
        info = {}
        info['username'] = self.get_current_user()
        self.render('search.html', info=info)

    def post(self):
        """
            user_word is the part of the word that the user has typed so far
        """
        user_string = self.get_argument("user_string", "")

        sql = "SELECT name FROM Activity WHERE name LIKE \'%s%\'" % (user_string)
        results = self.application.db.query(sql)

        dictionary = []
        print user_string
        for result in results:
            print result["name"]
            dictionary.append(result["name"])

        closest_match = nearest_word(user_string, dictionary)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"closest_word": closest_match}))
        self.finish()
