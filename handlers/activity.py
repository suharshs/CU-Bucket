from base import BaseHandler
import simplejson as json


class ActivityHandler(BaseHandler):

    def post(self):
        name = self.get_argument('name', '')
        description = self.get_argument('description', '')
        category = self.get_argument('category', '')
        location = self.get_argument('location', '')

        sql = """ INSERT INTO Activity (name, description, location, ranking) VALUES (\'%s\', \'%s\', \'%s\', 0) """ % (name, description, location)
        self.application.db.execute(sql)

        self.set_header("Content-Type", "application/json")
        was_successful = "true"
        self.write(json.dumps({"passed": was_successful}))
        self.finish()
