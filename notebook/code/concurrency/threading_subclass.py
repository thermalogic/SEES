import threading
import logging
import time
import datetime

class MyThread(threading.Thread):
    
    def run(self):
        time.sleep(2.0)
        str_curtime=datetime.datetime.now().strftime('%F %H:%M:%S.%f')
        logging.debug('running at '+ str_curtime)
        
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',)

def main():
    for i in range(5):
        t = MyThread()
        t.start() 

if __name__ == "__main__":
    main()
