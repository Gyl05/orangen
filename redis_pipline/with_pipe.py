import asyncio
import time 
import aioredis


async def without_pipe():
    pool = aioredis.ConnectionPool(**{
        'host': "localhost",
        'password': "redis123",
        'port': 6379,
    } )
    client = aioredis.Redis(connection_pool=pool)
    for i in range(1000):
        await client.lpush('task:100', i**2)
        await client.lpop('task:100')

async def with_pipe():
    pool = aioredis.ConnectionPool(**{
        'host': "localhost",
        'password': "redis123",
        'port': 6379,
    } )
    client = aioredis.Redis(connection_pool=pool)

    
    async with client.pipeline(transaction=True) as pipe:
        for i in range(1000):
            await pipe.lpush('task:100', i**2)
            await pipe.lpop('task:100')


    
async def main():
    # 分别用gather 和pipeline方式写入并删除1000条记录， 耗时悬殊
    t1 = time.perf_counter()
    await without_pipe()

    t2 = time.perf_counter()
    await with_pipe()

    cost1 = time.perf_counter() - t1
    cost2 = time.perf_counter() - t2

    print(cost1, cost2)

if __name__ == '__main__':
    asyncio.run(main())