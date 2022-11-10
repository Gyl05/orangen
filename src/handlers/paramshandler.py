from base.web import BaseRequestHandler, define_api


class ShowParamsHandler(BaseRequestHandler):
    def get(self):
        n1 = self.get_argument('name')
        n2 = self.get_arguments('id')
        n3 = self.get_argument('aa')
        n4 = self.get_argument('age')
        print(n1, n2, n3, n4)
        self.write('get ok')
    
    def post(self):
        self.write('post ok')