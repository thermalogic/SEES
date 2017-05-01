import timeit

t = timeit.Timer("print('main statement')", "print('setup')")

print('TIMEIT:')
print(t.timeit(2))

print('\n')
print('REPEAT:')
print(t.repeat(3, 2))
