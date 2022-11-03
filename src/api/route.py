from handlers.accounts import AccountsHandler
from handlers.hello import MainHandler


routers = [
    (r'/api/user', AccountsHandler),
    (r'/api/hello', MainHandler),
]