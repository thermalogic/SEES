program findroot

  implicit none

  real(8) :: x   ! solution variable
  real(8) :: xl  ! lower bound
  real(8) :: xr  ! upper bound
  real(8) :: f   ! final residual
  real(8) :: tol ! tolerance

  ! function declaration
  external myfun

  ! ask user for guess
  x=1.2

  ! ask for bounds
  xl=0.1
  xr=2.0

  ! ask for tolerance
  tol=0.01

  ! solve by bisection
  call bisect(myfun,xl,xr,x,f,tol)

  ! print result
  print *,'Solution is:',x,' with final residual:',f

  ! terminate the program
  stop

end program findroot
