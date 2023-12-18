function C(n,p) result(j)
    integer intent(in):: n
    integer intent (in):: p
    integer j

    if (p==0 .or. n==p) then
        j = 1

    else
        j = C(n-1,p) + C(n-1, p-1)

    endif
end function C


program calcul
integer :: n
integer :: p
integer C
character   :: arg_n
character  :: arg_p

call getarg(1, arg_n)
call getarg(2, arg_p)

read(arg_n, *) n
read(arg_p, *) p

    print* C(n,p)

end program calcul
