import redis as redis

# spring.redis.jedis.pool.max-active=20
# spring.redis.port=6379
# spring.redis.host=wan-dev-xinc818.redis.rds.aliyuncs.com
# spring.redis.password=pySR49e@2KsYIvwi
# spring.redis.database=1
redis_client = redis.Redis(host='wan-dev-xinc818.redis.rds.aliyuncs.com', password='pySR49e@2KsYIvwi')
redis_client.set('siwei', '四维')

print(redis_client.get('siwei').decode('utf-8'))
