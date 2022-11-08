
import json
import os


MYSQL_CONF_TEMP = {
    "host": "orangen-mysql",
    "user": "root",
    "password": "123456",
    "db": "orangen",
    "port": 3306
}

REDIS_CONF_TEMP = {
    "shard1":{
        "host": "orangen-redis-sts-0.orangen-redis",
        "password": "redis123",
        "port": 6379
    },
    "shard2":{
        "host": "orangen-redis-sts-1.orangen-redis",
        "password": "redis123",
        "port": 6379
    },
    "shard3":{
        "host": "orangen-redis-sts-2.orangen-redis",
        "password": "redis123",
        "port": 6379
    }
}

runtime_config_path = os.getenv('config-path')

if runtime_config_path:
    with open(runtime_config_path, 'r') as config:
        real_config = json.loads(config.read())

    MYSQL_CONF = real_config['MYSQL_CONF_TEMP']
    REDIS_CONF = real_config['REDIS_CONF_TEMP']

    print(MYSQL_CONF, REDIS_CONF)
else:
    MYSQL_CONF = {
        "host": "orangen-mysql",
        "user": "root",
        "password": "123456",
        "db": "orangen",
        "port": 3306
    },
    REDIS_CONF = {
        "shard1":{
            "host": "orangen-redis-0.orangen-redis",
            # "password": "redis123",
            "port": 6379
        },
        "shard2":{
            "host": "orangen-redis-1.orangen-redis",
            # "password": "redis123",
            "port": 6379
        },
        "shard3":{
            "host": "orangen-redis-2.orangen-redis",
            # "password": "redis123",
            "port": 6379
        }
    }