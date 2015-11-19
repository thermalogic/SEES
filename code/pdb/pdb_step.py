# encoding: utf-8


import pdb

def f(n):
    for i in range(n):
        j = i * n
        print(i, j)
    return

if __name__ == '__main__':
    pdb.set_trace()
    f(5)
