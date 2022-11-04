import time
from .base import BaseModel


class WebsiteModel(BaseModel):
    async def create_site(self, sitename, uri):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = f"""insert into `sites` (sitename, uri, create_time) 
        values('{sitename}', '{uri}', '{now}')"""
        msg, res = await self.execute_sql(sql)
        return msg, res
    
    async def get_all_site(self):
        sql = "select id, sitename, uri from `sites`"
        msg, res = await self.execute_sql(sql)
        return msg, res