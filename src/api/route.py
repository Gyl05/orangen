from handlers.accounts import AccountsHandler, VerifyCodeHandler
from handlers.hello import MainHandler
from handlers.accounts import LoginHandler
from handlers.sitehandler import WebSiteHandler
from handlers.filehandler import FileHandler


routers = [
    (r'/api/user', AccountsHandler),
    (r'/api/hello', MainHandler),
    (r'/api/login', LoginHandler),
    (r'/api/stored-sites', WebSiteHandler),
    (r'/api/vcode', VerifyCodeHandler),
    (r'/api/file', FileHandler)
]