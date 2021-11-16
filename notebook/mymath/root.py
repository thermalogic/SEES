def bisection(fun, y, xl, xr, tol, maxiter):
    """
       The program uses the bisection method to solve the equation
           f(x)-y = 0
       input:
         fun:the function(x)
         y : y=f(x)
         xl: lower bound
         xr: upper bound
         tol: tolerance
         maxiter： max iter
      return:   
           x;  solution 
           f : residual
           num_iters: the count of iters
    """
    fl = fun(xl)-y # residual for left  bound
    fr = fun(xr)-y # residual for right bound
    num_iters=0
    for i in range(maxiter):
        num_iters+=1
        
        # get midpoint
        x = 0.5*(xl + xr)
        
        # evaluate residual at midpoint
        f = fun(x)-y
        
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
    return x,f,num_iters  
    
