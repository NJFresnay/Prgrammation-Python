    recursive function C(n,p) result(ret)
        integer, intent (in) :: n
        integer, intent (in) :: p
        integer :: ret

        if (p==0 .or. n==p) then
            ret = 1
        else
            ret = C(n-1,p-1)+C(n-1,p)
        endif
    end function

    program racine
    integer :: n
    integer :: p
    integer :: C
    character(8)    :: cn
    character(8)    :: cp

    call getarg(1,cn)
    call getarg(2,cp)

    read(cn,*) n
    read(cp,*) p
        print*, C(n,p)

    end program racine
