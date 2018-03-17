
recursive function fib (n) result(f)

integer :: f
integer, intent(in) :: n

if (n==1) then
    f=0
else if (n==2) then
       f=1
     else
       f=fib (n-1)+fib (n-2)
endif

end function fib