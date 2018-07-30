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

    def post(self):
        vars_template = {
            'name': self.request.get('name'),
            'description': self.request.get('description'),
            'type': self.request.get('type'),
            'date': self.request.get('date'),
            'time_start': self.request.get('time_start'),
            'time_end': self.request.get('time_end'),
            'address': self.request.get('address'),
            'people_needed': self.request.get('people_needed')
        }
        confirm_template = JINJA_ENVIRONMENT.get_template('templates/confirm-event.html')
        self.response.write(form_template.render(vars_template))
        store = Event(name=vars_template['name'], description = vars_template['description'],
            type = vars_template['type'], date=vars_template['date'], time_start=vars_template['time_start'],
            time_end=vars_template['time_end'], address=vars_template['address'], people_needed=vars_template['people_needed'])
        k = store.put()
        print (k)
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
