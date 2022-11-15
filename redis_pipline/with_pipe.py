import asyncio
import time 
import aioredis


async def main():
    pool = aioredis.ConnectionPool(**{
        'host': "localhost",
        'password': "redis123",
        'port': 6379,
    } )
    client = aioredis.Redis(connection_pool=pool)

    t1 = time.perf_counter()
    for i in range(100):
        await client.lpush('task:100', i**2)
        await client.lpop('task:100')
        # async with client.pipeline(transaction=True) as pipe:
        #     # await pipe.lrange('task:100', 0 , -1)
        #     await pipe.lpush('task:100', i**2)
    
    cost = time.perf_counter() - t1

    print(cost)

if __name__ == '__main__':
    asyncio.run(main())