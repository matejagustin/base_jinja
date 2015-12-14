#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
from models import Message
from models import Todo
from models import Movie

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

class ForensicHandler(BaseHandler):
    def get(self):
        self.render_template("forensic.html")

    def post(self):
        dnk_enter = self.request.get("dnk_enter")
        dnk_enter = dnk_enter.upper()

        crni_lasje = "CCAGCAATCGC"
        rjavi_lasje = "GCCAGTGCCG"
        oranzni_lasje = "TTAGCTATCGC"
        kvadraten_obraz = "GCCACGG"
        okrogel_obraz = "ACCACAA"
        ovalen_obraz = "AGGCCTCA"
        modre_oci = "TTGTGGTGGC"
        zelene_oci = "GGGAGGTGGC"
        rjave_oci = "AAGTAGTGAC"
        moski = "TGCAGGAACTTC"
        zenska = "TGAAGGACCTTC"
        belec = "AAAACCTCA"
        crnec = "CGACTACAG"
        azijec = "CGCGGGCCG"

        face = ""
        hair = ""
        eyes = ""
        gender = ""
        rase = ""
        suspect = []
        error = ""

        if crni_lasje in dnk_enter:
            hair = "black hair"
            suspect.append(hair)
        elif rjavi_lasje in dnk_enter:
            hair = "brown hair"
            suspect.append(hair)
        elif oranzni_lasje in dnk_enter:
            hair = "orange hair"
            suspect.append(hair)

        if kvadraten_obraz in dnk_enter:
            face = "square face"
            suspect.append(face)
        elif okrogel_obraz in dnk_enter:
            face = "round face"
            suspect.append(face)
        elif ovalen_obraz in dnk_enter:
            face = "oval face"
            suspect.append(face)

        if modre_oci in dnk_enter:
            eyes = "blue eyes"
            suspect.append(eyes)
        elif zelene_oci in dnk_enter:
            eyes = "green eyes"
            suspect.append(eyes)
        elif rjave_oci in dnk_enter:
            eyes = "brown eyes"
            suspect.append(eyes)

        if moski in dnk_enter:
            gender = "male"
            suspect.append(gender)
        elif zenska in dnk_enter:
            gender = "female"
            suspect.append(gender)

        if belec in dnk_enter:
            rase = "white"
            suspect.append(rase)
        elif crnec in dnk_enter:
            rase = "afroamerican"
            suspect.append(rase)
        elif azijec in dnk_enter:
            rase = "asian"
            suspect.append(rase)


        if len(suspect) <= 0:
            error = "enter a valid dnk code"


        params = {"hair":hair,"face":face,"eyes":eyes,"gender":gender,"rase":rase,"suspect":suspect,"error":error}
        self.render_template("forensic.html",params=params)

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
        seznam = Message.query(Message.izbrisan == False).fetch()         # da prikazes samo tiste, ki niso izbrisani (v queriju)
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

class UrediSporociloHandler(BaseHandler):                       #ista koda, samo drugacen template in url
    def get(self,sporocilo_id):
        sporocilo = Message.get_by_id(int(sporocilo_id))
        params = {"sporocilo":sporocilo}
        return self.render_template("uredi_sporocilo.html",params=params)

    def post(self,sporocilo_id):
        vnos = self.request.get("vnos")
        sporocilo = Message.get_by_id(int(sporocilo_id))
        sporocilo.sporocilo = vnos

        sporocilo.put()

        self.redirect_to("seznam_sporocil")         #to je ta url iz handlerja (ne ime template)



class IzbrisiSporociloHandler(BaseHandler):
    def get(self,sporocilo_id):
        sporocilo = Message.get_by_id(int(sporocilo_id))
        params = {"sporocilo":sporocilo}
        return self.render_template("izbrisi_sporocilo.html",params=params)

    def post(self,sporocilo_id):                                # ce hocemo trajno zbrisat sporocilo: sporocilo.key.delete() in potem redirect
        sporocilo = Message.get_by_id(int(sporocilo_id))
        sporocilo.izbrisan = True

        sporocilo.put()

        self.redirect_to("seznam_sporocil")

########## TO-DO handlers.... ##########

class TodoHandler(BaseHandler):
    def get(self):
        return self.render_template("todo.html")

    def post(self):
        title = self.request.get("title")
        notes = self.request.get("notes")
        author = self.request.get("author")

        title = title.upper()

        task = Todo(naslov=title,datum=date,vsebina=notes,avtor=author)
        task.put()


        self.write(title)
        self.write(notes)
        self.write(author)


class TodoSeznamHandler(BaseHandler):
    def get(self):
        seznam = Todo.query(Todo.izbrisan == False).fetch()
        params = {"seznam":seznam}
        self.render_template("todo_seznam.html",params=params)


class TodoTaskDetailsHandler(BaseHandler):
    def get(self,task_id):
        task = Todo.get_by_id(int(task_id))
        params = {"task":task}
        self.render_template("todo_details.html",params=params)


class TodoIzpisHandler(BaseHandler):
    def get(self):
        self.render_template("todo_task.html")

    def post(self):
        title = self.request.get("title")
        notes = self.request.get("notes")
        author = self.request.get("author")

        title = title.upper()

        task = Todo(naslov=title,vsebina=notes,avtor=author)
        task.put()

        params = {"title":title,"notes":notes,"avtor":author}
        self.render_template("todo_task.html",params=params)


class TodoEditHandler(BaseHandler):                       #ista koda, samo drugacen template in url
    def get(self,task_id):
        task = Todo.get_by_id(int(task_id))
        params = {"task":task}
        return self.render_template("todo_uredi.html",params=params)

    def post(self,task_id):
        vnos = self.request.get("vnos")
        task = Todo.get_by_id(int(task_id))
        task.vsebina = vnos

        task.put()

        self.redirect_to("todo_seznam")         #to je ta url iz handlerja (ne ime template)



class TodoDeleteHandler(BaseHandler):
    def get(self,task_id):
        task = Todo.get_by_id(int(task_id))
        params = {"task":task}
        return self.render_template("todo_izbrisi.html",params=params)

    def post(self,task_id):                                # ce hocemo trajno zbrisat sporocilo: sporocilo.key.delete() in potem redirect
        task = Todo.get_by_id(int(task_id))
        task.izbrisan = True

        task.put()

        self.redirect_to("todo_seznam")


class TodoCompletedHandler(BaseHandler):
    def get(self,task_id):
        task = Todo.get_by_id(int(task_id))
        params = {"task":task}
        return self.render_template("todo_completed.html",params=params)

    def post(self,task_id):                                # ce hocemo trajno zbrisat sporocilo: sporocilo.key.delete() in potem redirect
        task = Todo.get_by_id(int(task_id))
        task.dokoncan = True

        task.put()

        self.redirect_to("todo_seznam")

class TestHandler(BaseHandler):
    def get(self):
        self.render_template("test.html")

    def post(self):
        test1 = self.request.get("test1")
        test2 = self.request.get("test2")
        test3 = self.request.get("test3")

        params = {"test1":test1,"test2":test2,"test3":test3}
        return self.render_template("test.html",params=params)


class MovieHandler(BaseHandler):

    def get(self):
        self.render_template("film.html")

    def post(self):
        title = self.request.get("title")
        url = self.request.get("url")
        rate = self.request.get("rate")

        movie = Movie(title=title,url=url,rate=rate)
        movie.put()

        self.write(title)
        self.write(url)
        self.write(rate)



class IzpisFilmaHandler(BaseHandler):
    def get(self):
        self.render_template("film_izpis.html")

    def post(self):
        title = self.request.get("title")
        url = self.request.get("url")
        rate = self.request.get("rate")

        movie = Movie(title=title,url=url,rate=rate)
        movie.put()


        params = {"title":title,"url":url,"movie":movie,"rate":rate}
        self.render_template("film_izpis.html",params=params)

class FilmSeznamHandler(BaseHandler):
    def get(self):
        filmi = Movie.query().fetch()
        params = {"filmi":filmi}
        return self.render_template("film_seznam.html",params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/contact',KontaktHandler),
    webapp2.Route('/projects',ProjectsHandler),
    webapp2.Route('/about',AboutHandler),
    webapp2.Route('/loto',LotoHandler),
    webapp2.Route('/calculator',CalculatorHandler),
    webapp2.Route('/capital',CapitalHandler),
    webapp2.Route('/hotel',MessageHandler),
    webapp2.Route('/seznam_sporocil',SeznamSporocilHandler, name="seznam_sporocil"),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>',SporociloHandler),
    webapp2.Route('/izpis',IzpisHandler),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>/uredi',UrediSporociloHandler),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>/izbrisi',IzbrisiSporociloHandler),
    webapp2.Route('/converter',ConverterHandler),
    webapp2.Route('/forensic',ForensicHandler),
    webapp2.Route('/todo',TodoHandler),
    webapp2.Route('/todo_task',TodoIzpisHandler),
    webapp2.Route('/todo_seznam',TodoSeznamHandler, name="todo_seznam"),
    webapp2.Route('/todo_details/<task_id:\d+>',TodoTaskDetailsHandler),
    webapp2.Route('/todo_details/<task_id:\d+>/edit',TodoEditHandler),
    webapp2.Route('/todo_details/<task_id:\d+>/delete',TodoDeleteHandler),
    webapp2.Route('/todo_details/<task_id:\d+>/completed',TodoCompletedHandler),
    webapp2.Route('/test',TestHandler),
    webapp2.Route('/film',MovieHandler),
    webapp2.Route('/film_izpis',IzpisFilmaHandler),
    webapp2.Route('/film_seznam',FilmSeznamHandler, name="film_seznam"),
], debug=True)
