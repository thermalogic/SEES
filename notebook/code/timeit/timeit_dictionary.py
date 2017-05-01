import timeit
import sys

# A few constants
range_size=1000
count=1000

setup_statement="l = [ (str(x), x) for x in range(%d) ]; d = {}" % range_size

print("%d items" % range_size)
print("%d iterations" % count)
print()

def show_results(result):
    "Print results in terms of microseconds per pass and per item."
    global count, range_size

    per_pass = 1000000 * (result / count)
    print('%.2f usec/pass' % per_pass,end='')

    per_item = per_pass / range_size
    print(' %.2f usec/item' % per_item)

# Using __setitem__ without checking for existing values first

print('__setitem__:\t',end='')
sys.stdout.flush()

# using setitem
t = timeit.Timer("""
for s, i in l:
    d[s] = i
""",
setup_statement)

show_results(t.timeit(number=count))

# Using setdefault
print('setdefault:\t',end='')
sys.stdout.flush()

t = timeit.Timer("""
for s, i in l:
    d.setdefault(s, i)
""",
setup_statement)
show_results(t.timeit(number=count))

# Using has_key
print('has_key:\t',end='')
sys.stdout.flush()

# using setitem
t = timeit.Timer("""
for s, i in l:
    if not (s in d):
        d[s] = i
""",
setup_statement)

show_results(t.timeit(number=count))

# Using exceptions
print('KeyError:\t',end='')

sys.stdout.flush()

# using setitem
t = timeit.Timer("""
for s, i in l:
    try:
        existing = d[s]
    except KeyError:
        d[s] = i
""",
setup_statement)

show_results(t.timeit(number=count))

# Using "in"
print('not in: \t',end='')

sys.stdout.flush()

# using setitem
t = timeit.Timer("""
for s, i in l:
    if s not in d:
        d[s] = i
""",
setup_statement)
show_results(t.timeit(number=count))
