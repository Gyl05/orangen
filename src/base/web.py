from tornado.web import RequestHandler
from base.mysql import BaseMysqlPool


class BaseRequestHandler(RequestHandler):

    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
    
    async def prepare(self):
        # check token
        allow_without_token_apis = [
            '/api/login',  # 登录接口不需要token，其他都需要登录
        ]

class BaseModel:
    def __init__(self) -> None:
        self.mysql_conn = None

    async def get_mysql_client(self):
        GlobalMysqlPool = BaseMysqlPool()
        self.mysql_conn = await GlobalMysqlPool.get_mysql_client()
        return self.mysql_conn
    
    async def execute_sql(self, sql):
        mysql_client = await self.get_mysql_client()
        async with mysql_client._conn.cursor() as cur:
            desc = await cur.execute(sql)
            queryset = await cur.fetchall()
        return desc, queryset


async def redis_mysql_prepare():
    GlobalMysqlPool = BaseMysqlPool()
    await GlobalMysqlPool.initialize()