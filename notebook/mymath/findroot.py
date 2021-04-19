def bisection(fun, k, xl, xr, tol, maxiter):
    """
      Input:
         fun: the function(k)
         k : the paraemeter of  fun
         xl: lower bound
         xr: upper bound
         tol: tolerance
         maxiter： max iter
      return:   
           x;  solution 
           f :final residual
           numIters: the count of iters
    """
    fl = fun(xl, k)
    fr = fun(xr, k)
    numIters = 0
    for i in range(maxiter):
        numIters += 1
        # get midpoint
        x = 0.5*(xl + xr)
        # evaluate resdiual at midpoint
        f = fun(x, k)
        #  check for convergence
        if (abs(f) < tol):
            break

       # reset the bounds
        if (f*fl < 0.0):
            # move right bound info to mid
            xr = x
            fr = f
        else:
            # move left bound info to mid
            xl = x
            fl = f
    return x, f, numIters
