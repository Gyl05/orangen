import json
import time
from base.redis import RedisFakeCluster


from base.web import BaseRequestHandler, Param, define_api
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
        self.write(return_dict)  # dict类型 tornado 自动转换json
        
    @define_api(
        name="新建账号",
        params=[
            Param('username', str, '账号'),
            Param('password', str, '密码')
        ],
        return_msg={
            "code": 200,
            "msg": "xxx"
        }
    )
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
        # username = self.get_argument('username')
        username = self.request.json_args['username']
        # password = self.get_argument('password')
        password = self.request.json_args['password']
        vcode_version = self.request.json_args['vcode-version']
        print(vcode_version)
        vcode = self.request.json_args['vcode']
        redis_client = await RedisFakeCluster().get_connection(vcode_version)
        vcode_redis = await redis_client.get(vcode_version)
        if vcode == vcode_redis.decode('utf-8'):
            account_ = await accountmodel.select_one(username)
            if account_:
                is_match = accountmodel.check_password(password, account_.get('password'))
                print(is_match)
                if is_match:
                    exp = int(time.time()) + 3600 * 8  # 登陆一次 token 有效期8h
                    username = account_.get('username')
                    payload = {'username': username, 'exp':str(exp)}
                    token = accountmodel.gen_token(payload)
                    await accountmodel.update_login_time(account_.get('id'))
                    self.write({"code": 200, "content":{"token": token, "username": username}})
                    # 查表， 发token  # TODO 接收参数，参数校验
                else:
                    self.write_error(status_code=401, message="用户名或密码错误")
            else:
                    self.write_error(status_code=401, message="用户名或密码错误")
        else:
            self.write_error(status_code=401, message="验证码错误")

class VerifyCodeHandler(BaseRequestHandler):
    async def get(self):
        accountmodel = AccountModel()
        scode_id, scode = await accountmodel.gen_identify_code(6)
        content = {'version': scode_id, 'scode': scode}
        self.write({'code':200, 'content': content})  # 把6位码返回