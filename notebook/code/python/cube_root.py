#  running use IDEL: tired of waiting
x=8
ans = 0  
while ans**3 < abs(x):
    ans = ans  # replace the statement ans = ans + 1 by ans = ans 
    # ans = ans + 1

if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,'is', ans)
