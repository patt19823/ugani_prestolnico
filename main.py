#!/usr/bin/env python
import os
import jinja2
import webapp2


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
        class Country_data:
            def __init__(self, country_name, country_capital, country_photo):
                self.name = country_name
                self.capital = country_capital
                self.photo = country_photo

        Germany = Country_data(country_name="Germany", country_capital="Berlin", country_photo="assets/photos/germany.jpg")
        Finland = Country_data(country_name="Finland", country_capital="Helskinki", country_photo="assets/photos/finland.jpg")
        Spain = Country_data(country_name="Spain", country_capital="Madrid", country_photo="assets/photos/spain")
        England = Country_data(country_name="England", country_capital="London", country_photo="assets/photos/england")
        Turkey = Country_data(country_name="Turkey", country_capital="Ankara", country_photo="assets/photos/turkey")


        countries_list = [Germany, Finland, Spain, England, Turkey]
        for drzava in countries_list:
            answer = drzava.name
            photo = drzava.photo

        view_vars = {
            "answer": answer,
            "photo": photo,
        }
        return self.render_template("hello.html", view_vars)

    def post(self):
        inserted_capital = self.request.get("inserted_capital")
        class Country_data:
            def __init__(self, country_name, country_capital, country_photo):
                self.name = country_name
                self.capital = country_capital
                self.photo = country_photo

        Germany = Country_data(country_name="Germany", country_capital="Berlin", country_photo="assets/photos/germany.jpg")
        Finland = Country_data(country_name="Finland", country_capital="Helskinki", country_photo="assets/photos/finland.jpg")
        Spain = Country_data(country_name="Spain", country_capital="Madrid", country_photo="assets/photos/spain")
        England = Country_data(country_name="England", country_capital="London", country_photo="assets/photos/england")
        Turkey = Country_data(country_name="Turkey", country_capital="Ankara", country_photo="assets/photos/turkey")

        countries_list = [Germany, Finland, Spain, England, Turkey]
        score = 0
        for drzava in countries_list:
            if inserted_capital.capitalize() == drzava.capital:
                score += 1
                respond = "Congrats"
            else:
                score = score
                respond = "You Dummy!"
        view_vars = {
            "score": score,
            "respond": respond,
        }

        return self.render_template("hello.html", view_vars)






app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
