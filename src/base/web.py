import json
import os
from tornado.web import RequestHandler
from base.mysql import BaseMysqlPool
from base.redis import RedisFakeCluster

from models.account import AccountModel

class LoggerMixin:
    pass

class BaseRequestHandler(RequestHandler):

    @property
    def content_type(self):
        return self.request.headers.get('Content-Type')

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

        content_type = self.content_type
        if content_type is not None and 'application/json' in content_type and self.request.body:
            try:
                json_args = json.loads(self.request.body)
                setattr(self.request, 'json_args', json_args)
            except Exception:
                print('bad application/json body', self.request.body)

        # check token
        allow_without_token_apis = [
            '/api/login',  # 登录接口不需要token，其他都需要登录
            '/api/vcode',
        ]
        token = self.request.headers.get('token', '')
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
        

LOCAL_DEBUG = os.getenv('LOCAL_DEBUG')
print(LOCAL_DEBUG, type(LOCAL_DEBUG))
if LOCAL_DEBUG == 'LOCAL':
    from config.local_config import MYSQL_CONF
    from config.local_config import REDIS_CONF
else:
    from config import MYSQL_CONF
    from config import REDIS_CONF

async def redis_mysql_prepare():
    GlobalMysqlPool = BaseMysqlPool()
    await GlobalMysqlPool.initialize(MYSQL_CONF)

    GlobalRedisFakeCluster = RedisFakeCluster()
    shard_num = await GlobalRedisFakeCluster.initialize(REDIS_CONF)
    print("RedisFakeCluster initializing...", shard_num)