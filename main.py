#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class KontaktHandler(BaseHandler):
    def get(self):
        return self.render_template("contact.html")

    def post(self):
        msg = self.request.get("sporocilo")
        prikaz = {"message":msg}
        return self.render_template("contact.html",params=prikaz)

class ProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("projects.html")

class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("about.html")

class LotoHandler(BaseHandler):
    def get(self):
        return self.render_template("loto.html")

    def post(self):
        xx = int(self.request.get("loto_stevilo"))

        random_range = range(0,39)
        generator = random.sample(random_range,xx)
        params = {"kombinacija":generator}
        return self.render_template("loto.html",params=params)

class CalculatorHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")

    def post(self):
        a = int(self.request.get("st1"))
        b = int(self.request.get("st2"))
        operacija = self.request.get("operacija")       #zdej smo poslal strezniku to, kar uporabnik vpise

        if operacija == "+":
            rezultat = a + b
        elif operacija == "*":
            rezultat = a * b
        elif operacija == "-":
            rezultat = a - b
        elif operacija == "/":
            rezultat = a / b

        params = {'rezultat': rezultat, "a":a, "b":b, "operacija":operacija}

        return self.render_template("calculator.html", params=params)



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


class CapitalHandler(BaseHandler,Capitals):
    def get(self):
        return self.render_template("capital.html")


    def post(self):

        france = Capitals(city = "Paris", state = "France", url = "/assets/img/paris.png")
        usa = Capitals(city = "Washington", state = "USA", url = "/assets/img/washington.png")
        egypt = Capitals(city = "Cairo", state = "Egypt", url = "/assets/img/cairo.png")
        italy = Capitals(city = "Rome", state = "Italy", url = "/assets/img/rome.png")
        uk = Capitals(city = "London", state = "UK", url = "/assets/img/london.png")

        states = [france, usa, egypt, italy, uk]


        drzava = random.choice(states)
        state = drzava.state
        capital = drzava.city
        url = drzava.url

        odgovor = self.request.get("odgovor")
        pravilen_odgovor = self.request.get("pravilen_odgovor")


        if odgovor == pravilen_odgovor:
            rezultat = "bravo"
        elif odgovor.lower() == pravilen_odgovor.lower():
            rezultat = "bravo"
        else:
            rezultat = "ni pravilno."


        params = {"state":state,"states":states,"capital":capital,"url":url,"rezultat":rezultat,"pravilen_odgovor":pravilen_odgovor}

        return self.render_template("capital.html",params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/contact',KontaktHandler),
    webapp2.Route('/projects',ProjectsHandler),
    webapp2.Route('/about',AboutHandler),
    webapp2.Route('/loto',LotoHandler),
    webapp2.Route('/calculator',CalculatorHandler),
    webapp2.Route('/capital',CapitalHandler),
], debug=True)
