
MYSQL_CONF = {
    "host": "orangen-mysql",
    'user': "root",
    "password": "123456",
    "db": "orangen",
    "port": 3306
}

REDIS_CONF = {
    'shard1':{
        'host': "orangen-redis-sts-0.orangen-redis",
        'password': "redis123",
        'port': 6379,
    },
    'shard2':{
        'host': "orangen-redis-sts-1.orangen-redis",
        'password': "redis123",
        'port': 6379,
    },
    'shard3':{
        'host': "orangen-redis-sts-2.orangen-redis",
        'password': "redis123",
        'port': 6379,
    }
}