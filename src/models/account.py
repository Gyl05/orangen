import time
from models import BaseModel 

class AccountModel(BaseModel):

    def parse_token(self, token):
        return None, 'parsed_info'
    
    def check_by_token_info(self, token_info):
        # 查表判断 token_info携带的信息是否和表中用户匹配
        user_info = {'uasename':'root'}
        return True, user_info

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
