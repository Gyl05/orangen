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

async def without_pipe():
    for i in range(LOOP):
        await client.lpush('task:100', i**2)
        await client.llen('task:100')
        await client.lpop('task:100')

async def normal_gather():
    coros = []
    for i in range(LOOP):
        coros.append(client.lpush('task:100', i**2))
        coros.append(client.llen('task:100'))
        coros.append(client.lpop('task:100'))
    await asyncio.gather(*coros)

async def with_pipe():
    async with client.pipeline(transaction=True) as pipe:
        for i in range(LOOP):
            await pipe.lpush('task:100', i**2)
            await pipe.llen('task:100')
            await pipe.lpop('task:100')


async def main():
    t1 = time.perf_counter()
    await with_pipe()

    t2 = time.perf_counter()
    await without_pipe()

    t3 = time.perf_counter()
    await normal_gather()

    cost1 = t2 - t1
    cost2 = t3 - t2
    cost3 = time.perf_counter() - t3

    print(cost1, cost2, cost3)

if __name__ == '__main__':
    asyncio.run(main())
    # LOOP=1000 => output: 0.007 2.808 3.652
