from google.appengine.ext import ndb

class Event(ndb.Model):
    name = ndb.StringProperty(required=True, default = "")
    title = ndb.StringProperty(required=True, default="")
    address = ndb.StringProperty(required=True, default="")
    type = ndb.StringProperty(required=True, default="")
    date = ndb.StringProperty(required=True)
    time_start = ndb.StringProperty(required=True) #need to learn how this works
    time_end = ndb.StringProperty(required=True)
    description = ndb.StringProperty(default="")
    people_needed = ndb.IntegerProperty(required=True, default=0)

class User(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty(required=True)

class Relation(ndb.Model):
    user_key = ndb.KeyProperty(User)
    event_key = ndb.KeyProperty(Event)
