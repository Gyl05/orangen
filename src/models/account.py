from hashlib import md5
import random
import time

import jwt
from base.redis import RedisFakeCluster
from models import BaseModel 

SECRET_KEY = 'SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

class Random_Code:
    def __init__(self, digitnum) -> None:
        self.version = str(time.time())
        self.digitnum = digitnum
        self.code = '0' * digitnum
    
    async def gen_code(self):
        self.code = ''.join([str(random.randint(0, 9)) for _ in range(self.digitnum)])
        redisclt = await RedisFakeCluster().get_connection(self.version)
        await redisclt.set(self.version, self.code, ex=120)
        return self.version, self.code

class AccountModel(BaseModel):

    async def gen_identify_code(self, num):
        # 生成一个验证码, 在redis存储、发送到用户邮箱
        random_code = Random_Code(num)
        scode_id, scode = await random_code.gen_code()
        # 生成redis中code的键 和值，把值发给用户邮箱，或者在前端展示，对比用户下一次输入和这个值
        return scode_id, scode

    def gen_token(self, payload):
        headers = {
        "alg": "HS256",
        "typ": "JWT",
        }
        key = SECRET_KEY
        token = jwt.encode(headers=headers, payload=payload, key=key)
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
        return passwd_tmp == db_passwd

    async def get_all_user(self):
        sql = "SELECT id, username, create_time FROM `user`;"
        msg, res = await self.execute_sql(sql)
        return res

    async def create_user(self, username, password):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        password = md5(password.encode('utf-8')).hexdigest()
        sql = f"""INSERT INTO `user` 
        (username, password, create_time, update_time) 
        values('{username}', '{password}' , '{now}', '{now}');"""
        print(sql)
        msg, res = await self.execute_sql(sql)
        print(msg, res)
        return msg, res
    
    async def select_one(self, val):
        if isinstance(val, int):
            sql = f"SELECT * FROM `user` where id='{val}';"
        else:
            sql = f"SELECT * FROM `user` where username='{val}';"
        msg, res = await self.execute_sql(sql)
        if isinstance(res, list) and res:
            return res[0]
    
    async def update_login_time(self, uid):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = f"UPDATE `user` SET update_time = '{now}' where id = '{uid}';"
        msg, res = await self.execute_sql(sql)
        print(msg, res)
        return msg, res 
