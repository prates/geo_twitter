import redis

conn = redis.StrictRedis(host='localhost', port=6379, db=0)
[ conn.delete(i) for i in conn.keys("*") ]
