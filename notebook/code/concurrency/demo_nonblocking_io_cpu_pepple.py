import sys  
sys.path.append('./code/')  

from nonblocking_io_cpu_pepple import get_data_with_timeout

if __name__ == '__main__':
    timeout=3
    rc,value=get_data_with_timeout(timeout)
    print(rc,value)
