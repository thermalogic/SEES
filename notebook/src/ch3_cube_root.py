# Test in IDEL By ch3_cube_root
x=8
ans = 0  
while ans**3 < abs(x):
    
    ans = ans  # replace the statement ans = ans + 1 by ans = ans 
               # 4.Its value is decreased every time through the loop. 
               # 3.When its value is <=0, the loop terminates. 

if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,'is', ans)