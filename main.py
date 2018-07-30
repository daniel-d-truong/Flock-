import webapp2
import jinja2
import os
from google.appengine.ext import ndb

class Events(ndb.model):
    name = ndb.StringProperty(required=True, default = "")
    title = ndb.StringProperty(required=True, default="")
    address = ndb.StringProperty(required=True, default="")
    type = ndb.StringProperty(required=True, default="")
    date = ndb.DateProperty(required=True, default="")
    time_start = ndb.TimeProperty(required=True, default="") #need to learn how this works
    time_end = ndb.TimeProperty(required=True, default="")
    description = ndb.StringProperty(default = "")

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler): #main page
    def get(self):
        self.response.write('Hello World')

class HostEventHandler(webapp2.RequestHandler): #making events
    def get(self):
        self.response.write('Write down info in order to host your event.')

class FindEventHandler(webapp2.RequestHandler): #newsfeed and searching for events
    def get(self):
        self.response.write('Let\'s find an event!!')

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/form', HostEventHandler),
    ('/newsfeed', FindEventHandler)
], debug=True)
