program circle_test

  use class_Circle, only: Circle,circle_print

  implicit none

  type(Circle) :: acircle  ! a circle instance

  acircle%radius=3.2
 
  write(*,'("The radius is:",T30,F0.4)') acircle%radius
  ! print out results
  call circle_print(acircle)

  ! terminate the program
  stop

end program circle_test
