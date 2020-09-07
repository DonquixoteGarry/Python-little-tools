while 1:
    print("----------------------- 素数检验器   NEW SOLUTION -----------------------")
    a=eval(input("\ntest:    "))
    num=0
    b=int(a/2+1)
    elem="it can be divided by "
    for i in range(2,b):
        flag=0
        if int(a//i)*i==a:
            flag=1
            a=int(a/i)
            if(a!=1):
                elem=elem+str(i)+" , "
            else:
                elem=elem+str(i)
        num=num+flag
    elem=elem+" \n\nThat's all\n"
    if num==0:
        print("\n>>>Yes,it is a prime\n")
    else:
        print("\n>>>No,it is never a prime\n\n"+elem+"\n")
