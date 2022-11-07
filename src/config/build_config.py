
MYSQL_CONF = {
    "host": "orangen-mysql",
    'user': "root",
    "password": "123456",
    "db": "orangen",
    "port": 3306
}

REDIS_CONF = {
    'shard1':{
        'host': "orange-redis0.orange-redis",
        'password': "redis123",
        'port': 6379,
    },
    'shard2':{
        'host': "orange-redis1.orange-redis",
        'password': "redis123",
        'port': 6379,
    },
    'shard3':{
        'host': "orange-redis2.orange-redis",
        'password': "redis123",
        'port': 6379,
    }
}