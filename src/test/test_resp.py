# 执行各类sql语句之后 的返回值是什么，所需要的信息去哪里取

import aiomysql
import asyncio


conn_conf = {
    "host": "localhost",
    "db": "orangen",
    "user": "root",
    "password": "123456",
    "cursorclass": aiomysql.cursors.DictCursor,
    "autocommit": True,
}


async def fetchall():
    loop = asyncio.get_running_loop()
    conn = await aiomysql.connect(**conn_conf, loop=loop)
    cur = await conn.cursor()
    await cur.execute("select sitename, id from `sites`;")
    desc, content = cur.description, await cur.fetchall()
    print(desc, content, sep='\n')

async def fetchone():
    loop = asyncio.get_running_loop()
    conn = await aiomysql.connect(**conn_conf, loop=loop)
    cur = await conn.cursor()
    await cur.execute("select sitename, id from `sites` where id=2")
    desc, content = cur.description, await cur.fetchone()
    print(desc, content, sep='\n')

async def create_one():
    loop = asyncio.get_running_loop()
    conn = await aiomysql.connect(**conn_conf, loop=loop)
    cur = await conn.cursor()
    exe_res = await cur.execute("insert into `sites` (sitename, uri) values ('aiomysql', 'https://aiomysql.readthedocs.io/en/latest/');")
    desc, content = cur.description, await cur.fetchone()
    print(f'rowcount {cur.rowcount}, lastrowid {cur.lastrowid}')

async def main():
    # await fetchall()
    # await fetchone()
    await create_one()
    await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())