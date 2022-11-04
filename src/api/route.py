from handlers.accounts import AccountsHandler
from handlers.hello import MainHandler
from handlers.accounts import LoginHandler
from handlers.sitehandler import WebSiteHandler

routers = [
    (r'/api/user', AccountsHandler),
    (r'/api/hello', MainHandler),
    (r'/api/login', LoginHandler),
    (r'/api/stored-sites', WebSiteHandler),
]