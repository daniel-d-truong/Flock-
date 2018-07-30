import webapp2
import jinja2
import os
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World')

class HostEventHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Write down info in order to host your event.')

class FindEventHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Let\'s find an event!!')

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/form', HostEventHandler),
    ('/newsfeed', FindEventHandler)
], debug=True)
