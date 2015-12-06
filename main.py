#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
from models import Message

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

        is_visible = True
        params = {"is_visible":is_visible}

        return self.render_template("capital.html",params=params)

    def post(self):

        france = Capitals(city = "Paris", state = "France", url = "/assets/img/paris.png")
        usa = Capitals(city = "Washington", state = "USA", url = "/assets/img/washington.png")
        egypt = Capitals(city = "Cairo", state = "Egypt", url = "/assets/img/cairo.png")
        italy = Capitals(city = "Rome", state = "Italy", url = "/assets/img/rome.png")
        uk = Capitals(city = "London", state = "UK", url = "/assets/img/london.png")
        greece = Capitals(city = "Athens", state = "Greece", url = "/assets/img/athens.png")
        china = Capitals(city = "Beijing", state = "China", url = "/assets/img/beijing.png")
        belgium = Capitals(city = "Brussels", state = "Belgium", url = "/assets/img/brussels.png")
        turkey = Capitals(city = "Ankara", state = "Turkey", url = "/assets/img/ankara.png")
        india = Capitals(city = "Delhi", state = "India", url = "/assets/img/delhi.png")

        states = [france, usa, egypt, italy, uk, greece, china, belgium, turkey, india]

        drzava = random.choice(states)
        state = drzava.state
        capital = drzava.city
        url = drzava.url

        is_visible = False

        pricni = self.request.get("pricni")

        odgovor = self.request.get("odgovor")
        pravilen_odgovor = self.request.get("pravilen_odgovor")


        if odgovor == pravilen_odgovor:
            rezultat = "Correct."
        elif odgovor.lower() == pravilen_odgovor.lower():
            rezultat = "Correct."
        else:
            rezultat = "Not correct."


        params = {"state":state,"states":states,"capital":capital,"url":url,"rezultat":rezultat,"pravilen_odgovor":pravilen_odgovor,"is_visible":is_visible,"pricni":pricni}

        return self.render_template("capital.html",params=params)

class MessageHandler(BaseHandler):

    def get(self):
        self.render_template("hotel.html")

    def post(self):
        name = self.request.get("ime")
        email = self.request.get("mail")
        message = self.request.get("sporocilo")

        whole_message = Message(ime=name,mail=email,sporocilo=message)
        whole_message.put()

        self.write(name)
        self.write(email)
        self.write(message)


class SeznamSporocilHandler(BaseHandler):
    def get(self):
        seznam = Message.query().fetch()
        params = {"seznam":seznam}
        return self.render_template("seznam_sporocil.html",params=params)

class SporociloHandler(BaseHandler):
    def get(self,sporocilo_id):
        sporocilo = Message.get_by_id(int(sporocilo_id))
        params = {"sporocilo":sporocilo}
        self.render_template("sporocilo.html",params=params)

class IzpisHandler(BaseHandler):
    def get(self):
        self.render_template("izpis.html")

    def post(self):
        name = self.request.get("ime")
        email = self.request.get("mail")
        message = self.request.get("sporocilo")


        whole_message = Message(ime=name,mail=email,sporocilo=message)
        whole_message.put()

        params = {"name":name, "email":email,"message":message}
        self.render_template("izpis.html",params=params)

class ConverterHandler(BaseHandler):
    def get(self):
        self.render_template("converter.html")

    def post(self):

        try:

            unit = self.request.get("select")
            unit2 = self.request.get("select2")
            number = float(self.request.get("number"))
            result = 0.0

            if unit == "mm" and unit2 == "mm":
                result = number * 1
            if unit == "mm" and unit2 == "cm":
                result = number / 10
            elif unit == "mm" and unit2 == "m":
                result = number / 1000
            elif unit == "mm" and unit2 == "km":
                result = number / 1000000
            elif unit == "cm" and unit2 == "cm":
                result = number * 1
            elif unit == "cm" and unit2 == "mm":
                result = number * 10
            elif unit == "cm" and unit2 == "m":
                result = number / 100
            elif unit == "cm" and unit2 == "km":
                result = number / 100000
            elif unit == "m" and unit2 == "m":
                result = number * 1
            elif unit == "m" and unit2 == "mm":
                result = number * 1000
            elif unit == "m" and unit2 == "cm":
                result = number * 100
            elif unit == "m" and unit2 == "km":
                result = number / 1000
            elif unit == "km" and unit2 == "km":
                result = number * 1
            elif unit == "km" and unit2 == "mm":
                result = number * 1000000
            elif unit == "km" and unit2 == "cm":
                result = number * 100000
            elif unit == "km" and unit2 == "m":
                result = number * 1000
            else:
                result == False
                error = "Can not convert %s to %s" % (unit, unit2)

            if unit == "g" and unit2 == "kg":
                result = number / 1000
            elif unit == "g" and unit2 == "t":
                result = number / 1000000
            elif unit == "g" and unit2 == "g":
                result = number * 1
            elif unit == "kg" and unit2 == "g":
                result = number * 1000
            elif unit == "kg" and unit2 == "t":
                result = number / 1000
            elif unit == "kg" and unit2 == "kg":
                result = number * 1
            elif unit == "t" and unit2 == "g":
                result = number * 1000000
            elif unit == "t" and unit2 == "kg":
                result = number * 1000
            elif unit == "t" and unit2 == "t":
                result = number * 1
            else:
                result == False
                error = "Can not convert %s to %s" % (unit, unit2)


            params = {"result":result,"unit":unit,"unit2":unit2,"number":number,"error":error}

            self.render_template("converter.html",params=params)

        except:
            unit = self.request.get("select")
            valueError = "Please enter a valid number!"
            params = {"valueError":valueError,"unit":unit}
            self.render_template("converter.html",params=params)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/contact',KontaktHandler),
    webapp2.Route('/projects',ProjectsHandler),
    webapp2.Route('/about',AboutHandler),
    webapp2.Route('/loto',LotoHandler),
    webapp2.Route('/calculator',CalculatorHandler),
    webapp2.Route('/capital',CapitalHandler),
    webapp2.Route('/hotel',MessageHandler),
    webapp2.Route('/seznam_sporocil',SeznamSporocilHandler),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>',SporociloHandler),
    webapp2.Route('/izpis',IzpisHandler),
    webapp2.Route('/converter',ConverterHandler),
], debug=True)
