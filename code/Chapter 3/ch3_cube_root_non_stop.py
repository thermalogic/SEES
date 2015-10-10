x=8
ans = 0  
while ans**3 < abs(x):
    print('Value of the decrementing function abs(x) - ans**3 is',\
          abs(x) - ans**3)  # add the statement at the start of the loop
                            # test whether the decrementing function is indeed being decremented
    ans = ans  # replace the statement ans = ans + 1 by ans = ans 
               # 4.Its value is decreased every time through the loop. 
               # 3.When its value is <=0, the loop terminates. 

if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,'is', ans)
