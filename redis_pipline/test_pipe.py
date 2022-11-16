import asyncio
import time 
import aioredis

LOOP = 1000

redis_conf = {
    'host': "localhost",
    'password': "redis123",
    'port': 6379,
}
pool = aioredis.ConnectionPool(**redis_conf )
client = aioredis.Redis(connection_pool=pool)

async def test():
    await client.get('msg')

async def test1():
    async with client.pipeline() as pipe:
        await pipe.get('msg')

async def main():
    t0 = time.time()
    await test()

    t1 = time.time()
    await test1()

    t2 = time.time()

    print(t1-t0, t2-t1)

if __name__ == '__main__':
    asyncio.run(main())
