from base import BaseHandler
import simplejson as json

class ActivityHandler(BaseHandler):

    def post(self):
        name = self.get_argument('name', '')
        description = self.get_argument('description', '')

        sql = """ INSERT INTO  """
        self.application.db.execute(sql)

        self.set_header("Content-Type", "application/json")
        was_successful = "true"
        self.write(json.dumps({"passed": was_successful}))
        self.finish()

