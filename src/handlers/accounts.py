import json
import time


from base.web import BaseRequestHandler
from models.account import AccountModel

class AccountsHandler(BaseRequestHandler):

    async def get(self):
        accountmodel = AccountModel()
        users = await accountmodel.get_all_user()
        for user in users:
            user['create_time'] = user['create_time'].strftime("%Y-%m-%d %H:%M:%S")
        return_dict = {
            'code': 200,
            'content': users
        }
        json_str = json.dumps(return_dict, ensure_ascii=False)
        self.write(json_str)
    
    async def post(self):
        username = 'kkktest'
        password = '334455'
        accountmodel = AccountModel()
        await accountmodel.create_user(username, password)  # TODO 新增用户接口的返回格式？
        self.write('create user ok.')


class LoginHandler(BaseRequestHandler):

    def post(self):
        # 查表， 发token
        self.write('登录成功')