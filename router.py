import webapp2

app = webapp2.WSGIApplication(
    routes = [
        webapp2.Route('/', handler='app.main.MainClass')
    ], debug=True)
