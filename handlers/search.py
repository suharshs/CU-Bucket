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
        words = self.application.trie.check_prefix(user_string)
        results = []
        if words:
            names = ""
            for word in words:
                names = names + '\"' + word + '\"'
                if word != words[len(words) - 1]:
                    names = names + ", "
            sql = """SELECT * FROM Activity
            LEFT JOIN (SELECT userName as interestUserName, activityID FROM UserInterest WHERE userName='%s') as currUserInterest
            ON Activity.ID = currUserInterest.activityID
            LEFT JOIN (SELECT userName as completedUserName, activityID FROM UserCompleted WHERE userName='%s') as currUserComplete
            ON Activity.ID = currUserComplete.activityID
            WHERE name LIKE \'%s%s%s\' ORDER BY Activity.ID DESC LIMIT 0, 20""" % (self.get_current_user(), self.get_current_user(), "%", user_string, "%")
            print sql
            results = self.application.db.query(sql)
            print results

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"matches": results, "username": self.get_current_user()}))
        self.finish()

        """
        user_string = self.get_argument("user_string", "")
        print user_string
        sql = "SELECT name FROM Activity"
        print sql
        results = self.application.db.query(sql)
        print results
        dictionary = []
        print user_string
        for result in results:
            print result["name"]
            dictionary.append(result["name"])

        if (len(dictionary) == 0):
            closest_match = " "
        else:
            closest_match = nearest_word(user_string, dictionary)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"closest_word": closest_match}))
        self.finish()
        """
