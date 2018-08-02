from google.appengine.ext import ndb

class Event(ndb.Model):
    name = ndb.StringProperty(required=True, default = "")
    #title = ndb.StringProperty(required=True, default="")
    address = ndb.StringProperty(required=True, default="")
    type = ndb.StringProperty(required=True, default="")
    date = ndb.StringProperty(required=True)
    time_start = ndb.StringProperty(required=True) #need to learn how this works
    time_end = ndb.StringProperty(required=True)
    description = ndb.StringProperty(default="")
    people_needed = ndb.IntegerProperty(required=True, default=0)
    #created_at = ndb.DateTimeProperty(required=True)

class Profile(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    id = ndb.StringProperty(required=True)

class Relation(ndb.Model):
    user_key = ndb.KeyProperty(Profile)
    event_key = ndb.KeyProperty(Event)
