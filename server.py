import os
import sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import urlparse
from tornado.database import Connection
from tornado.options import options, define

from handlers.login import *
from handlers.user import *
from handlers.signup import *
from handlers.activity import *
from handlers.home import *

PORT = sys.argv[1]
DATABASE_URL = sys.argv[2]

define("port", default=PORT, help="run on the given port", type=int)
define("debug", default=True, help="run tornado in debug mode", type=bool)


class Application(tornado.web.Application):
    def __init__(self):

        #url = urlparse.urlparse(DATABASE_URL)
        #self.db = Connection(host=url.hostname, user=url.username, password=url.password, database=url.path[1:])
        self.db = Connection(host="engr-cpanel-mysql.engr.illinois.edu", user="cubucket_root", password="cucket", database="cubucket_db")
        # in other files we can refer to this with self.application.db, maintains one db connection

        handlers = [
            tornado.web.URLSpec(r'/', LoginHandler),
            tornado.web.URLSpec(r'/login', LoginHandler),
            tornado.web.URLSpec(r'/logout', LogoutHandler),
            tornado.web.URLSpec(r'/signup', SignupHandler),
            tornado.web.URLSpec(r'/activity/new', ActivityHandler),
            tornado.web.URLSpec(r'/user/([a-zA-Z0-9-_]+)', UserHandler),
            tornado.web.URLSpec(r'/home', HomeHandler)
        ]

        current_dir = os.path.dirname(__file__)

        settings = dict(
            template_path=os.path.join(current_dir, 'templates'),
            static_path=os.path.join(current_dir, 'static'),
            debug=options.debug,
            autoescape='xhtml_escape',
            cookie_secret='Dxj43jWAKSag/JbQTmIbBWvpSlBkazj6YGo0A0mo5tyZkb4sTUvT3UH4GU9SXgFuy=',
            xsrf_cookies='True'
        )

        super(Application, self).__init__(handlers, **settings)

        logging.info('Server started on port {0}'.format(options.port))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
