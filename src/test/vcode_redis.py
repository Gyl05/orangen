import asyncio
import requests
from base.redis import RedisFakeCluster
from base.web import redis_mysql_prepare

async def test():
    resp = requests.get('http://127.0.0.1:8000/api/vcode')
    content = resp.json().get('content')
    version_key = content['version']
    scode = content['scode']
    await redis_mysql_prepare()
    redis_client = await RedisFakeCluster().get_connection(version_key)
    code_redis = await redis_client.get(version_key)
    code_redis = code_redis.decode('utf-8')
    print(code_redis, scode)
    assert code_redis == scode

if __name__ == '__main__':
    asyncio.run(test())

