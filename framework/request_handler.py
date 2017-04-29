import os
import webapp2
import jinja2

class SearchRequestHandler(webapp2.RequestHandler):

    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)),
        'templates')

    jinja_enviroment = jinja2.Environment(
        loader = jinja2.FileSystemLoader(template_dir)
    )

    def render(self,template, **kwargs):
        jinja_template = self.jinja_enviroment.get_template(template)
        html_from_template = jinja_template.render(kwargs)
        self.response.out.write(html_from_template)
