import aioredis


from base.utils import Singleton


class PoolUninitExcption(Exception):
    def __repr__(self) -> str:
        return "连接池未初始化"


class RedisClient:
    def __init__(self, conn: aioredis.Redis) -> None:
        self._conn = conn
    
    def __del__(self):
        self._conn = None
    
    async def set(self, key, val):
        return await self._conn.set(key, val)
    
    async def get(self, key):
        return await self._conn.get(key)
    
    async def lpush(self, lname, *vals):
        return await self._conn.lpush(lname, *vals)
    
    async def lrange(self, key, start=0, end=-1):
        return await self._conn.lrange(key, start, end)


class BaseRedisPool():
    def __init__(self) -> None:
        self._pool = None
    
    async def init_pool(self, redis_conf):
        conf = {
            'host': "localhost",
            'password': "redis123",
            'port': 6379,
        }
        conf.update(redis_conf)
        self._pool = await aioredis.ConnectionPool(**conf)
    
    async def get_connection(self):
        if not self._pool:
            raise PoolUninitExcption  
        conn = aioredis.Redis(connection_pool=self._pool)
        return RedisClient(conn)
    
    async def info(self):
        info = "<>"

REDIS_CONF = {
    'shard1':{
        'host': "127.0.0.1",
        'password': "redis123",
        'port': 6379,
    }
}

class RedisFakeCluster(Singleton):
    def __init__(self) -> None:
        self.shards = []
        self.shard_num = 0

    def initialize(self, conf):
        for shard_name, conf in REDIS_CONF:
            self.shards.append(BaseRedisPool(**conf))
        self.shard_num =  len(self.shards)
        return self.shard_num
    
    def select_slot(self, token):
        # 根据token，分发对应 连接池上的一个连接
        if not isinstance(token, str):
            raise ValueError("expect an string")
        hashsum = sum([ord(chr) for chr in token])
        dest_pool_id = hashsum % self.shard_num
        return dest_pool_id
    
    def get_connection(self, token):
        hash_id = self.select_slot(token)
        pool = self.shards[hash_id]
        conn = pool.get_connection()