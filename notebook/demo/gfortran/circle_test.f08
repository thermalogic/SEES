program circle_test

  use class_Circle, only: Circle,circle_print

  implicit none

  type(Circle) :: acircle  ! a circle instance

  acircle%radius=3.2

  call circle_print(acircle)
 
  ! print out  results
  PRINT '("The radius is:",T30,F0.4,/,&
           "The area is:",T30,F0.4,/,&
           "The circumference is:",T30,F0.4)', &
             acircle%radius, acircle%area,acircle%circum

end program circle_test
