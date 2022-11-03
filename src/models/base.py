from base.mysql import BaseMysqlPool


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