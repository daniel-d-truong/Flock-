import webapp2
import jinja2
import os
from models import Event, User, Relation
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler): #main page
    def get(self):
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

class HostEventHandler(webapp2.RequestHandler): #making events
    def get(self):
        self.response.write('Write down info in order to host your event.')
        form_template = JINJA_ENVIRONMENT.get_template('templates/form.html')
        self.response.write(form_template.render())

class FindEventHandler(webapp2.RequestHandler): #newsfeed and searching for events
    def get(self):
        self.response.write('Let\'s find an event!!')
        newsfeed_template = JINJA_ENVIRONMENT.get_template('templates/newsfeed.html')
        self.response.write(newsfeed_template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/form', HostEventHandler),
    ('/newsfeed', FindEventHandler)
], debug=True)
