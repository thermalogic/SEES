import time
import psutil
import pebble 
from concurrent.futures import TimeoutError

def get_data():
    time.sleep(0.5)
    return psutil.cpu_percent()

def get_data_with_timeout(timeout=1):
    pool = pebble.ProcessPool(max_workers=1)
    future = pool.schedule(get_data, args=(), timeout=timeout)
    try:
        result = future.result()
        rc = 1
        value = result
    except TimeoutError:
        rc = 0
        value = None
    except Exception as error:
        rc = 0
        value = None
        print(error)
    return (rc, value)


if __name__ == '__main__':
    rc,value = get_data_with_timeout(0.1)
    print(rc,value)
