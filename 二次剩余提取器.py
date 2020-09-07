while 1:
    print("\n----------------------- 二次剩余提取器   NEW SOLUTION -----------------------")
    mod=eval(input("\nmod:    "))
    a=set()
    b=set()
    for i in range(1,mod):
        num=i**2
        num=num-mod*(num//mod)
        a.add(num)
        b.add(i)
    c=b-a
    QR=list(a)
    nonQR=list(c)
    print("\n>>>QR:","\n",QR,"\n",end="")
    print("\n>>>nonQR:","\n",nonQR,"\n")
