import sys  
sys.path.append('./code/concurrency/')  

from nonblocking_io_cpu import get_data_with_timeout

if __name__ == '__main__':
    timeout=3.0                   
    rc,value=get_data_with_timeout(timeout)
    print(rc,value)
