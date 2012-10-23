from base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, username):
        info = {'username': username}
        print '"' + username + '"'
        #self.render('user.html', info=info)

        if (self.get_current_user() == username or username == ''):
            info = {'username': self.get_current_user()}
            self.render('user.html', info=info)
            # this is the user's personal page so we will show them all of the info
            pass
        else:
            # public user page, not everything is shown
            pass
