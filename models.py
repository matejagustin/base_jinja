from google.appengine.ext import ndb

class Message(ndb.Model):
    ime = ndb.StringProperty(required=False)
    mail = ndb.StringProperty(required=False)
    sporocilo = ndb.StringProperty(required=True)
    nastanek = ndb.DateProperty(auto_now_add=True)
