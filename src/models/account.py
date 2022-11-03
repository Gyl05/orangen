import time
from base.web import BaseModel 

class AccountModel(BaseModel):

    async def get_all_user(self):
        sql = "SELECT id, username, create_time FROM `user`;"
        msg, res = await self.execute_sql(sql)
        print(msg, res)
        return res

    
    async def create_user(self, username, password):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = f"""INSERT INTO `user` 
        (username, password, create_time, update_time) 
        values('{username}', '{password}' , '{now}', '{now}');"""
        print(sql)
        msg, res = await self.execute_sql(sql)
        # print(msg, res)
        