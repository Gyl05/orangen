import jwt


class SingletonMetaclass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        result = None

        instances = cls.__class__._instances
        if cls in instances:
            result = instances[cls]
        else:
            result = instances[cls] = super().__call__(*args, **kwargs)

        return result


class Singleton(metaclass=SingletonMetaclass):

    def __init__(self) -> None:
        pass


class Util:
    def jwt_encode(self, payload: dict, secret: str) ->bytes:
        return jwt.encode(payload, secret, algorithm='HS256')

    def jwt_decode(self, jwt_str: str, secret: str) ->dict:
        try:
            payload = jwt.decode(jwt_str, secret)
        except jwt.PyJWKError:
            payload = None
        return payload