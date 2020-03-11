function myfun(x)

  implicit none

  ! formal variables
  real(8) :: myfun   ! the function declaration, residual
  real(8) :: x       ! the independent variable

  myfun = x**2 - 4

end function myfun
