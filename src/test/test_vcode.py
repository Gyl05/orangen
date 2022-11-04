import asyncio
from models.account import AccountModel
from base.web import redis_mysql_prepare

async def test():
    await redis_mysql_prepare()
    accountmodel = AccountModel()
    await accountmodel.gen_identify_code(5)
    await asyncio.sleep(30)

if __name__ == '__main__':
    asyncio.run(test())