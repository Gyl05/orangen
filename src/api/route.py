from handlers.accounts import AccountsHandler
from handlers.hello import MainHandler
from handlers.accounts import LoginHandler


routers = [
    (r'/api/user', AccountsHandler),
    (r'/api/hello', MainHandler),
    (r'/api/login', LoginHandler),
]