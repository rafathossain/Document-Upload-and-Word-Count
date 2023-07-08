#!/bin/bash

redis_ready() {
  python <<END
import sys
from redis import Redis
try:
    redis_host = '${REDIS_HOST}'
    r = Redis(redis_host, socket_connect_timeout=1)
    r.ping()
except Exception as e:
    sys.exit(-1)
sys.exit(0)
END
}
