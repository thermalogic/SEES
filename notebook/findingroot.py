def bisection(func,low,high,k,epsilon):
    ans = (high + low)/2.0
    numGuesses = 0
    while abs(func(ans,k)) >= epsilon:
        numGuesses += 1
        if ans**2 < k:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans,numGuesses
