import aiomysql
import asyncio

async def test_mysql():
    conf = {
        'host': 'localhost',
        'user': 'root',
        'password': '123456',
        'db': 'orangen'
    }
    mysqlpool = await aiomysql.create_pool(**conf, loop=asyncio.get_running_loop())
    conn = await mysqlpool.acquire()
    cur = await conn.cursor()
    sql = "SELECT id, username, create_time FROM `user`;"
    await cur.execute(sql)
    res = await cur.fetchall()
    print(res)

async def main():
    await test_mysql()
    await asyncio.sleep(20)


if __name__ == '__main__':
    asyncio.run(main())