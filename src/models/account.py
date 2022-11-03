from hashlib import md5
import time

import jwt
from models import BaseModel 

SECRET_KEY = 'SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'


class AccountModel(BaseModel):
    
    def gen_token(self, payload):
        headers = {
        "alg": "HS256",
        "typ": "JWT",
        }
        key = SECRET_KEY
        token = jwt.encode(headers=headers, payload=payload, key=key)
        print(type(token))

        return token

    def parse_token(self, token):
        res = {}
        try:
            res = jwt.decode(jwt=token, key=SECRET_KEY, algorithms='HS256')
        except Exception as e:
            print(e)
        finally:
            return None, res
    
    async def check_by_token_info(self, token_info):
        # 查表判断 token_info携带的信息是否和表中用户匹配
        username = token_info.get('username')
        account_ = await self.select_one(username)
        if account_:
            return True, account_
        else:
            return False, None
    
    def check_password(self, send_passwd, db_passwd):
        # send_passwd
        passwd_tmp = md5(send_passwd.encode('utf-8')).hexdigest()
        print(passwd_tmp, db_passwd, sep='\n')
        return passwd_tmp == db_passwd

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
    
    async def select_one(self, val):
        if isinstance(val, int):
            sql = f"SELECT * FROM `user` where id='{val}';"
        else:
            sql = f"SELECT * FROM `user` where username='{val}';"
        msg, res = await self.execute_sql(sql)
        return res[0]
    
