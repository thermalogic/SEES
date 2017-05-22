
print(__debug__)

mylist = ['item']
assert(len(mylist) >= 1)
mylist.pop()
try:
    assert (len(mylist) >= 1),'mylist<1'
except AssertionError as err:
    print('AssertionError',err)

if not (__debug__) :
    print('__debug__ is',__debug__ ,'so that no :err mylist<1') 
else:
    print('__debug__ is',__debug__ ,'so that:err:',err) 