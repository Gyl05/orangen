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
        username = self.get_argument('username')
        password = self.get_argument('password')
        accountmodel = AccountModel()
        existed = await accountmodel.select_one(username)
        if existed:
            self.write_error(status_code=401, message='账号已存在')
        else:
            await accountmodel.create_user(username, password)  # TODO 新增用户接口的返回格式？
            self.write('create user ok.')


class LoginHandler(BaseRequestHandler):

    async def post(self):
        accountmodel = AccountModel()
        username = self.get_argument('username')
        password = self.get_argument('password')
        account_ = await accountmodel.select_one(username)
        if account_:
            is_match = accountmodel.check_password(password, account_.get('password'))
            print(is_match)
            if is_match:
                exp = int(time.time()) + 3600
                username = account_.get('username')
                payload = {'username': username, 'exp':str(exp)}
                token = accountmodel.gen_token(payload)
                await accountmodel.update_login_time(account_.get('id'))
                self.write({"code": 200, "content":{"token": token, "username": username}})
                # 查表， 发token  # TODO 接收参数，参数校验
            else:
                self.write_error(status_code=401, message="用户名或密码错误")

class VerifyCodeHandler(BaseRequestHandler):
    async def get(self):
        accountmodel = AccountModel()
        accountmodel.gen_identify_code()