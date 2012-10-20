from base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, username):
        info = {'username': username}
        print 'UserHandler'
        self.render('user.html', info=info)

        """ The idea here is that we will show all of the information if
        username is equal to self.current_user
        otherwise we will show a limited view of the profile. """
