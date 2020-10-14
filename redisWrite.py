import redis
from datetime import datetime
import time
import random
r = redis.Redis(host='localhost', port=6379, db=0)
# r.set('foo', 'bar')


lastDate = datetime.now()

while True:
    randomData = random.random()*10
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)
    r.set(str(current_time), str(randomData))
    # print (r.get(str(current_time)))
    time.sleep(1)