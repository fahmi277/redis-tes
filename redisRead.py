import redis
r = redis.Redis("localhost", 6379)
for key in r.scan_iter():
       print (key)