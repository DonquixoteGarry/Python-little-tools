while 1:
    print("----------------------- 线性同余方程求解器   NEW SOLUTION -----------------------")
    a=eval(input("\n左系数:    "))
    b=eval(input("\n右数:    "))
    mod=eval(input("\n模数:    "))
    for i in range(0,mod):
        s=a*i
        flag=b-(s-mod*(s//mod))
        if flag==0:
        	print("\n>>>X≡",i,"(mod ",mod,")")