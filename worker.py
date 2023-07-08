import os

import redis
from dotenv import load_dotenv
from rq import Worker

# Loading variable from env file
load_dotenv()

# Worker queue
listen = ['default']

redis_url = os.getenv('REDIS_URL', 'redis://192.168.10.11:6379')

# Creating redis connection
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    # Starting RQ Worker
    w = Worker(listen, connection=conn)
    w.work()
