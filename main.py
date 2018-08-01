import webapp2
import jinja2
import os
#import stream
import json
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
        self.response.write(welcome_template.render({'login_url': users.create_login_url('/')}))

class HostEventHandler(webapp2.RequestHandler): #making events
    def get(self):
        template_var = {} //logout
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            template_var = {
                "logout_url": logout_url,
                "nickname": nickname
            }
        else:
            self.redirect('/')
        form_template = JINJA_ENVIRONMENT.get_template('templates/form.html')
        self.response.write(form_template.render(template_var))

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
            'people_needed': int (self.request.get('people_needed')),
            #'created_at':
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
        list_of_events = Event.query().fetch()
        # print (list_of_events)
        html_vars= {

        }

        for item in range(len(list_of_events)):
            html_vars[list_of_events[item].put()] = list_of_events[item]

        for i in html_vars:
            temp_event = html_vars[i]
            # self.response.write('<div style=height:300px>' + temp_event.name + temp_event.title + temp_event.address
            #     + temp_event.type + temp_event.date + temp_event.time_start + temp_event.time_end + temp_event.description
            #     + str(temp_event.people_needed) + '</div>')
            # self.response.write('<br>')
        self.response.write(newsfeed_template.render())

#class SignUpHandler(webapp2.RequestHandler)

class RetrieveEventsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = 'text/json'
        new_events = Event.query().fetch()
        new_events_list = []
        for i in new_events: #i is the event object that is an element
            new_events_list.append({
                'name': i.name,
                'description': i.description,
                'type': i.type,
                'date': i.date,
                'time_start': i.time_start,
                'time_end': i.time_end,
                'address': i.address,
                'people_needed': i.people_needed,
            #'created_at':
            })
        self.response.write(json.dumps(new_events_list))



app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/form', HostEventHandler),
    ('/confirm', ShowConfirmationHandler),
    ('/newsfeed', FindEventHandler),
    ('/retrieve', RetrieveEventsHandler)
], debug=True)
