import threading
import time
import logging

def daemon():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

start_time = time.time()
d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()
d.join()
t.join()
print(threading.current_thread().name+" Exiting!")
print('Total Time：', time.time()-start_time)
