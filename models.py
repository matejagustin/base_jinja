from google.appengine.ext import ndb

class Message(ndb.Model):
    ime = ndb.StringProperty(required=False)
    mail = ndb.StringProperty(required=False)
    sporocilo = ndb.StringProperty(required=True)
    nastanek = ndb.DateProperty(auto_now_add=True)
    izbrisan = ndb.BooleanProperty(default=False)

class Todo(ndb.Model):
    naslov = ndb.StringProperty()
    avtor = ndb.StringProperty()
    vsebina = ndb.StringProperty()
    nastanek = ndb.DateProperty(auto_now_add=True)
    izbrisan = ndb.BooleanProperty(default=False)
    dokoncan = ndb.BooleanProperty(default=False)

class Movie(ndb.Model):
    title = ndb.StringProperty()
    url = ndb.StringProperty()
    rate = ndb.StringProperty()
