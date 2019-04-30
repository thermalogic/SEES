"""
  https://blog.csdn.net/MeteorCountry/article/details/82765919
"""
import psutil
import time
import threading

class IOThread(threading.Thread): 
    
    def __init__(self,target,args=()):  
        super(IOThread,self).__init__()
        self.func = target
        self.args = args
        
    def run(self):
        self.result = self.func(*self.args) 
            
    def get_result(self):
        try:   
            return self.result
        except Exception:
            return None

def timeout_decor(timeout): 
    """ timeout: max time,s  
        return: if timeout ,return None 
    """ 
    def functions(func): 
    
        def run(*params):
            thre_func = IOThread(target=func,args=params)
            # if timeout,main thread stop,then the iothread is stoped 
            thre_func.setDaemon(True)
            thre_func.start()
            sleep_num = int(timeout // 1)
            sleep_nums = round(timeout % 1, 1) 
            for i in range(sleep_num):
                time.sleep(1)
                infor = thre_func.get_result()
                if infor:
                    return infor
            time.sleep(sleep_nums)
            return thre_func.get_result()       
            
        return run
    
    
    return functions

def get_data_with_timeout(timeout):
    @timeout_decor(timeout)
    def get_data():
        time.sleep(2)
        return psutil.cpu_percent()        
    
    value=get_data()
    if value is not None:
        rc=1 # ok
    else: 
        rc=0 # timeout
    return (rc,value)    

if __name__ == '__main__':
    timeout=3.0                   
    rc,value=get_data_with_timeout(timeout)
    print(rc,value)
