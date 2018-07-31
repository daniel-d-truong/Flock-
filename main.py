import webapp2
import jinja2
import os
from models import Event, User, Relation
from google.appengine.ext import ndb
from google.appengine.api import users

events_dict = {

}

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
        form_template = JINJA_ENVIRONMENT.get_template('templates/form.html')
        self.response.write(form_template.render())

class ShowConfirmationHandler(webapp2.RequestHandler): #after event is made
    def post(self):
        vars_template = {
            'name': self.request.get('name'),
            'description': self.request.get('description'),
            'type': self.request.get('type'),
            'date': self.request.get('date'),
            'time_start': self.request.get('time_start'),
            'time_end': self.request.get('time_end'),
            'address': self.request.get('address'),
            'people_needed': int (self.request.get('people_needed'))
        }
        confirm_template = JINJA_ENVIRONMENT.get_template('templates/confirm-event.html')
        self.response.write(confirm_template.render(vars_template))
        store = Event(name=vars_template['name'], description = vars_template['description'],
            type = vars_template['type'], date=vars_template['date'], time_start=vars_template['time_start'],
            time_end=vars_template['time_end'], address=vars_template['address'], people_needed=vars_template['people_needed'])
        key = store.put()

class FindEventHandler(webapp2.RequestHandler): #newsfeed and searching for events
    def get(self):
        newsfeed_template = JINJA_ENVIRONMENT.get_template('templates/newsfeed.html')
        self.response.write(newsfeed_template.render())
        list_of_events = Event.query().fetch()
        # print (list_of_events)
        html_vars= {

        }

        for item in range(len(list_of_events)):
            html_vars[list_of_events[item].put()] = list_of_events[item]

        for i in html_vars:
            self.response.write((html_vars[i]))
            self.response.write('<br>')

#class SignUpHandler(webapp2.RequestHandler)

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/form', HostEventHandler),
    ('/confirm', ShowConfirmationHandler),
    ('/newsfeed', FindEventHandler)
], debug=True)
