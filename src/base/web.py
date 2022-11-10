import json
import os
from typing import Dict, List
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
    
    def get_argument(self, name, default=None):
        try:
            arg = super().get_argument(name)
        except Exception:
            if hasattr(self.request, 'json_args'):
                arg = self.request.json_args.get(name, default)
            else:
                arg = default
        return arg
    
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
            '/api/hello',
            '/api/stored-sites',
            '/api/show_params'
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
    from config.build_config import MYSQL_CONF
    from config.build_config import REDIS_CONF

async def redis_mysql_prepare():
    GlobalMysqlPool = BaseMysqlPool()
    await GlobalMysqlPool.initialize(MYSQL_CONF)

    GlobalRedisFakeCluster = RedisFakeCluster()
    shard_num = await GlobalRedisFakeCluster.initialize(REDIS_CONF)
    print("RedisFakeCluster initializing...", shard_num)


class Param:  # HTTP传递的参数 query body
    def __init__(self, name, type, label, required=False, default=None, description=None) -> None:
        self.required = required  # 是否必须
        self.name = name  # 参数名称
        self.description = description  # 描述
        self.label = label
        self.type = type
        self.default = default
    
    def check(self, val):  # 检查参数类型
        # 能此处，参数一定在要求列表中
        if isinstance(val, str):
            if self.type is int:
                return int(val)
            elif self.type is float:
                return float(val)
            elif self.type is bool:
                return val.upper() == 'TRUE'
        elif isinstance(val, dict):
            return json.loads(val)
        else:
            return val

class API:  # 生成api接口文档
    def __init__(self, apiname, params, return_msg) -> None:
        self.name = apiname
        self.params = params
        self.return_msg = return_msg

    def parse_request_params(self, request):
        parserd_params = {}
        try:
            for param in self.params:
                param_in_request = request.get_argument(param.name, None)
                parsed = param.check(param_in_request)
                parserd_params[param.name] = parsed
            request.params = parserd_params
        except Exception as e:
            return '参数错误'

def define_api(name: str, params: List[Param], return_msg: Dict):
    # 返回一个装饰器
    def wrapper(async_func):  # 返回一个improved 协程
        async def wrapped_func(requesthandler: RequestHandler, *args, **kwargs):
            api = API(name, params, return_msg)
            error_msg = api.parse_request_params(requesthandler)
            if error_msg:
                return requesthandler.write_error({'code': 500, 'msg': '参数错误'})
            await async_func(requesthandler, *args, **kwargs)
        return wrapped_func
    return wrapper