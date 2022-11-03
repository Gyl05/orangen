from tornado.web import RequestHandler
from base.mysql import BaseMysqlPool
from base.redis import REDIS_CONF, RedisFakeCluster
from models.account import AccountModel


class BaseRequestHandler(RequestHandler):

    def write_error(self, message, status_code):

        self.set_status(status_code)

        _json = {
            "error": {
                "status": status_code,
                "details": [message]
            }
        }
        self.write(_json)

    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
    
    async def prepare(self):
        # check token
        allow_without_token_apis = [
            '/api/login',  # 登录接口不需要token，其他都需要登录
        ]
        token = self.request.headers.get('token', '')
        print('携带的token:', token)
        if not token and self.request.path not in allow_without_token_apis:
            self.write_error(status_code=401, message="未登录1")
            return self.finish()

        if self.request.path not in allow_without_token_apis:
            accountmodel = AccountModel()
            error_code, token_info = accountmodel.parse_token(token)
            if error_code or not token_info:
                self.write_error(status_code=401, message="未登录2")
                return self.finish()

            if error_code is None and token_info:
                user_checked, user_info = await accountmodel.check_by_token_info(token_info)
                if user_checked:
                    self.user_info = user_info
        
        

async def redis_mysql_prepare():
    GlobalMysqlPool = BaseMysqlPool()
    await GlobalMysqlPool.initialize()

    GlobalRedisFakeCluster = RedisFakeCluster()
    shard_num = await GlobalRedisFakeCluster.initialize(REDIS_CONF)
    print("RedisFakeCluster initializing...", shard_num)