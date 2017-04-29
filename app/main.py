from framework.request_handler import SearchRequestHandler

class MainClass(SearchRequestHandler):
    def get(self):
        self.render('home/index.html')
