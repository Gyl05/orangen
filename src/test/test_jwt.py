import jwt
from models.account import AccountModel

SECRET_KEY = 'SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

def gen_token(payload):
    headers = {
        "alg": "HS256",
        "typ": "JWT",
    }
    key = SECRET_KEY
    token = jwt.encode(headers=headers, payload=payload, key=key)
    print(type(token))
    return token

def parse_token(token):
    res = jwt.decode(jwt=token, key=SECRET_KEY, algorithms='HS256')
    print(res, type(res))
    return res

if __name__=='__main__':
    payload = {
        'username': 'root'
    }
    # token = gen_token(payload)
    # parse_token(token)
    accountmodel = AccountModel()
    token = accountmodel.gen_token(payload)
    res = accountmodel.parse_token(token)
