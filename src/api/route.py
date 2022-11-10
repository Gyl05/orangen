from handlers.accounts import AccountsHandler, LoginHandler, VerifyCodeHandler
from handlers.filehandler import FileHandler
from handlers.hello import MainHandler
from handlers.paramshandler import ShowParamsHandler  # 对传入参数做展示echo
from handlers.sitehandler import WebSiteHandler

routers = [
    (r'/api/user', AccountsHandler),
    (r'/api/hello', MainHandler),
    (r'/api/login', LoginHandler),
    (r'/api/stored-sites', WebSiteHandler),
    (r'/api/vcode', VerifyCodeHandler),
    (r'/api/file', FileHandler),

    (r'/api/show_params', ShowParamsHandler)
]