subroutine bisect(fun,xl,xr,x,f,tol)

implicit none

  ! arguments
  real(8),intent(inout) :: xl       ! left bound
  real(8),intent(inout) :: xr       ! right bound
  real(8),intent(inout) :: x        ! result
  real(8),intent(out)   :: f        ! residual
  real(8),intent(in)    :: tol      ! residual tolerance

  ! function argument
  real(8) :: fun
  external fun

  ! local varaibles
  real(8) :: fl     ! residual for left  bound
  real(8) :: fr     ! resdiual for right bound
  integer :: i      ! loop counter

  ! determine residual bounds
  fl = fun(xl)
  fr = fun(xr)

  ! begin loop
  do i = 1,100

    ! get midpoint
    x = 0.5_8*(xl + xr)

    ! evaluate resdiual at midpoint
    f = fun(x)

    ! check for convergence
    if (abs(f) < tol) exit

    ! reset the bounds
    if (f*fl < dble(0.0)) then

      ! move right bound info to mid
      xr = x
      fr = f

    else

      ! move left bound info to mid
      xl = x
      fl = f

    end if


    ! print out information
    print *,'Iteration:',i,' Residual:',f

  end do

end subroutine bisect
