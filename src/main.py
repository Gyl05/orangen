import asyncio
import tornado.web


from api.route import routers
from base.web import redis_mysql_prepare


def make_app():
    return tornado.web.Application(
        routers
    )

async def main():
    await redis_mysql_prepare()
    app = make_app()
    app.listen(8000)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
