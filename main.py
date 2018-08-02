import webapp2
import jinja2
import os
#import stream
import time
import json
from models import Event, Profile, Relation
from google.appengine.ext import ndb
from google.appengine.api import users

new_events_list = []

#
# }

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class PutUserHandler(webapp2.RequestHandler):
    def post(self):
        us = users.get_current_user()
        template_vars={
            'first_name': self.request.get('firstname'),
            'last_name': self.request.get('lastname'),
            'city': self.request.get('city'),
            'state': self.request.get('state'),
            'id': users.get_current_user().user_id()
        }

        new_profile=Profile(first_name=template_vars['first_name'], last_name=template_vars['last_name'],
            city=template_vars['city'], state=template_vars['state'], id=template_vars['id'])

        print "wowww"
        new_profile.put()
        time.sleep(0.5)
        self.redirect('/')

class WelcomeHandler(webapp2.RequestHandler): #main page
    def get(self):
        us = users.get_current_user()
        print (Profile.id)
        print (us.user_id())
        current_users=Profile.query(Profile.id==us.user_id()).fetch()
        # print current_users
        if current_users==[]:
            template=JINJA_ENVIRONMENT.get_template('templates/user-signup.html')
            self.response.write(template.render())
        else:
            welcome_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
            self.response.write(welcome_template.render({'login_url': users.create_login_url('/')}))

    # def post(self):
    #
    #     welcome_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
    #     self.response.write(welcome_template.render({'login_url': users.create_login_url('/')}))


class HostEventHandler(webapp2.RequestHandler): #making events
    def get(self):
        template_var = {} #logout
        # user = users.get_current_user()
        # print user
        # if user:
        #     nickname = user.nickname()
        #     logout_url = users.create_logout_url('/')
        #     template_var = {
        #         "logout_url": logout_url,
        #         "nickname": nickname
        #     }
        # else:
        #     self.redirect('/')
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
        self.redirect('/newsfeed')
class FindEventHandler(webapp2.RequestHandler): #newsfeed and searching for events
    def get(self):
        newsfeed_template = JINJA_ENVIRONMENT.get_template('templates/newsfeed.html')
        self.response.write(newsfeed_template.render())

#class SignUpHandler(webapp2.RequestHandler)

class RetrieveEventsHandler(webapp2.RequestHandler):
    def get(self):
        activity_type = self.request.get('type')
        self.response.content_type = 'text/json'
        if activity_type:
            print "We're filtering"
            new_events = Event.query(Event.type == activity_type).fetch()
        else:
            print "We're getting everything"
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
                'event_id': i.key.id()

            #'created_at':
            })
        self.response.write(json.dumps(new_events_list))

class AddUserToEvent(webapp2.RequestHandler):
    def get(self):
        key = int((self.request.get('k'))) #event key
        event_key = ndb.Key(Event, key)
        main_event = Event.query(event_key == Event.key).get()
        logged_in_user = users.get_current_user()
        prof = Profile.query(logged_in_user.user_id() == Profile.id).get()
        new_relation = Relation(user_key = prof.key, event_key=main_event.key)
        current_relation = Relation.query(ndb.AND(Relation.user_key==prof.key, Relation.event_key==main_event.key)).get()


        if current_relation == None:
            new_relation.put()
            time.sleep(.5)

        user_events = Relation.query(Relation.event_key == event_key).fetch()
        profiles = []

        for u in user_events:
            profile = u.user_key.get()
            profiles.append(profile)
        profiles.sort()
        template=JINJA_ENVIRONMENT.get_template('templates/event.html')
        self.response.write(template.render(Profile=profiles, event=main_event))
        #new_relation.put()

        print prof
        print ""
        print main_event
        print current_relation
        print user_events

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/form', HostEventHandler),
    ('/confirm', ShowConfirmationHandler),
    ('/newsfeed', FindEventHandler),
    ('/retrieve', RetrieveEventsHandler),
    ('/putuser', PutUserHandler),
    ('/event', AddUserToEvent)
], debug=True)
