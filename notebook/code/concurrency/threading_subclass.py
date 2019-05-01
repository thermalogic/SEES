import threading
import logging
import time
import datetime

class MyThread(threading.Thread):
    
    def run(self):
        str_curtime=datetime.datetime.now().strftime('%H:%M:%S.%f')
        logging.debug('begin at '+ str_curtime)
        time.sleep(2.0)
        str_curtime=datetime.datetime.now().strftime('%H:%M:%S.%f')
        logging.debug('  end at '+ str_curtime)
        
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',)

def main():
    for i in range(5):
        t = MyThread()
        t.start() 

if __name__ == "__main__":
    main()
