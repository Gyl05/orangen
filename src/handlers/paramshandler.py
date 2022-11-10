from base.web import BaseRequestHandler, define_api


class ShowParamsHandler(BaseRequestHandler):
    def get(self):
        self.write('get ok')
    
    def post(self):
        self.write('post ok')