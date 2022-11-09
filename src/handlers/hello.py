import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world 666, your IP is: {}".format(self.request.remote_ip))