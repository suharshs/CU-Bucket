from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


class MobileHandler(RequestHandler):
    def check_xsrf_cookie(self):
        pass
