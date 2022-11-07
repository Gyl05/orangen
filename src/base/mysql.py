import aiomysql
import asyncio


from base.utils import Singleton
from config import MYSQL_CONF

class MysqlClient:
    def __init__(self, conn, pool) -> None:
        self._conn = conn
        self._pool = pool

    def __del__(self):
        try:
            print('[MYSQL POOL] usage {} / {}'.format(self._pool.size - self._pool.freesize, self._pool.size))
            self._pool.release(self._conn)
        finally:
            print('[MYSQL POOL] usage {} / {}'.format(self._pool.size - self._pool.freesize, self._pool.size))
            self._pool = None
            self._conn = None
            


class BaseMysqlPool(Singleton):
    def __init__(self) -> None:
        self._pool = None

    async def initialize(self, MYSQL_CONF):
        mysql_conf = {
            'minsize': 2,
            'maxsize': 4,
            'echo': True,
            'cursorclass': aiomysql.cursors.DictCursor,
            'autocommit': True,
        }
        mysql_conf.update(MYSQL_CONF)
        loop = asyncio.get_running_loop()
        self._pool = await aiomysql.create_pool(**mysql_conf, loop=loop)
    
    async def get_mysql_client(self):
        print('[MYSQL POOL] usage {} / {}'.format(self._pool.size - self._pool.freesize, self._pool.size))
        conn = await self._pool._acquire()
        return MysqlClient(conn, self._pool)