
function MYFUNCTION(a,b)
    !GCC$ ATTRIBUTES DLLEXPORT,STDCALL:: MYFUNCTION
    integer*2 ::  a,b
    integer*2 ::  MYFUNCTION
    MYFUNCTION = a-b
end function