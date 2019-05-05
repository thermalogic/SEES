from concurrent.futures import ThreadPoolExecutor
import time
import psutil

def virtual_interface_data(tag):
    time.sleep(1)
    monitoringios={"CPU_PERCENT": psutil.cpu_percent(),
                   "MEM_PERCENT": psutil.virtual_memory().percent,
                   "BAT_PERCENT": psutil.sensors_battery().percent} 
    try:              
        value= monitoringios[tag]
        rc=1    
    except:
        rc,value=0,None  
    return (rc,value)        

def get_data_with_timeout(timeout=1,tag=None):
    pool=ThreadPoolExecutor(max_workers=1)
    future = pool.submit(virtual_interface_data,tag)
    try: 
        rc,value = future.result(timeout=timeout)
    except TimeoutError:
        rc = 0
        value = None
    except Exception as error:
        rc = 0
        value = None
    return (rc, value)
