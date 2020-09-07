while 1:
    print("----------------------- 幂次同余方程求解器   NEW SOLUTION -----------------------")
    t=eval(input("\n幂次数:    "))
    rv=eval(input("\n右值:    "))
    mod=eval(input("\n模数:    "))
    num=1
    for i in range(2,mod):
        a=i**t
        a=a-mod*(a//mod)
        flag=rv-a
        if flag==0:
            print("\n>>>X≡",i,"(mod ",mod,")")