import random

class Capitals():
    city = "city"
    state = "state"
    url = "url"

    def __init__(self,city,state,url):
        self.city = city
        self.state = state
        self.url = url

    def __str__(self):
        return ("city: %s,  state: %s, url: %s") % (self.city, self.state, self.url)

france = Capitals(city = "Paris", state = "France", url = "/assets/img/paris.png")
usa = Capitals(city = "Washington", state = "USA", url = "/assets/img/washington.png")
egypt = Capitals(city = "Cairo", state = "Egypt", url = "/assets/img/cairo.png")
italy = Capitals(city = "Rome", state = "Italy", url = "/assets/img/rome.png")

states = [france, usa, egypt, italy]

state = states(state.city)
print state










