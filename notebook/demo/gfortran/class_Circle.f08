module class_Circle

  implicit none
  private
  public :: circle_print

  real :: pi = 3.1415926535897931D0 ! module-wide private constant

  type, public :: Circle

    real :: radius ! the radius of a circle
    real :: area   ! the area of a circle
    real :: circum ! the circumference of a circle

  end type Circle

contains

!==============================================================================
! CIRCLE_AREA calculates the area of a circle
!==============================================================================

  function circle_area(this) result(area)

    type(Circle), intent(in)  :: this ! circle instance
    real                      :: area ! the area of the circle

    ! calculate the area
    area = pi * this%radius**2

  end function circle_area

!==============================================================================
! CIRCLE_CIRCUM calculate the circumference of a circle
!==============================================================================

  function circle_circum(this) result(circum)

    type(Circle), intent(in) :: this   ! circle instance
    real                     :: circum ! the circumference

    ! calculate circumference
    circum = 2*pi*this%radius

  end function circle_circum

!==============================================================================
! CIRCLE_PRINT prints information about the circle
!==============================================================================

  subroutine circle_print(this)

    type(Circle), intent(inout) :: this ! circle instance

    ! calculate area
    this%area = circle_area(this)

    ! calculate circumference
    this%circum = circle_circum(this)

    ! print results
    write(*,'("The area is:",T30,F0.4,/,"The circumference is:",T30,F0.4)')    &
   &           this%area,this%circum

  end subroutine circle_print

end module class_Circle
